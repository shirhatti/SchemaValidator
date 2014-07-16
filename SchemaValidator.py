import sublime, sublime_plugin
import threading
import urllib.request
import json
import os, sys
import re

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import jsonschema

class Loading():
    def __init__(self, view, status_message, display_message, callback):
        self.view = view
        self.i = 0
        self.dir = 1
        self.status_message = status_message
        self.display_message = display_message
        self.callback = callback
    def increment(self):
        before = self.i % 8
        after = (7) - before
        if not after:
            self.dir = -1
        if not before:
            self.dir = 1
        self.i += self.dir
        self.view.set_status(self.status_message, " [%s=%s]" % \
                (" " * before, " " * after))
        sublime.set_timeout(lambda: self.callback(), 100)
    def clear(self):
        self.view.erase_status(self.status_message)
        pass

class ValidateSchemaCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.thread = ValidateSchema(self.window.active_view())
        self.thread.start()
        self.loading = Loading(self.window.active_view(), "match_schema", "Matching File to schema", self.handle_thread)
        self.handle_thread()
    def handle_thread(self):
        if self.thread.is_alive():
            self.loading.increment()
            return
        self.loading.clear()
        if self.thread.result == False:
            sublime.status_message(self.thread.message)
        elif self.thread.result == True:
            sublime.status_message(self.thread.message)
        else:
            sublime.status_message("Something went wrong. Please try again")
        return

class ValidateSchema(threading.Thread):
    def __init__(self,view):
        self.result = None
        self.message = None
        self.view = view
        threading.Thread.__init__(self)
    def run(self):
        # Check for valid JSON
        try:
            json_data = json.loads(self.view.substr(sublime.Region(0, self.view.size())))
        except ValueError as e:
            self.message = "Not valid JSON file"
            self.result = False
            return
        # Check for schema in document
        try:
            schema_url = json_data['$schema']
            self.message = schema_url
            self.result = True
        # If no schema attribute was found, let's try a file match
        except (KeyError, TypeError) as e:
            try:
                request = urllib.request.Request("http://schemastore.org/api/json/catalog.json", headers={"User-Agent": "Sublime"})
                http_file = urllib.request.urlopen(request, timeout=5)
                http_response = http_file.read().decode("utf-8")
                try:
                    catalog = json.loads(http_response)["schemas"]
                except ValueError as e:
                    self.message = "Retrieved schema is not a valid JSON file"
                    self.result = False
                    return
                except LookupError as e:
                    self.message = "Catalog.json contains no schemas"
                    self.result = False
            except (urllib.request.HTTPError) as e:
                self.message = "%s: HTTP error %s contacting API" % (__name__, str(e.code))
                self.result = False
                return
            except (urllib.request.URLError) as e:
                self.message = "%s: URL error %s contacting API" % (__name__, str(e.reason))
                self.result = False
                return
            try:
                file_name = self.view.file_name()[self.view.window().folders()[0].__len__()+1:]
            except IndexError as e:
                file_name = self.view.file_name()
                if file_name == "":
                    self.message = "Try adding a $schema attribute to your file or try saving your file"
            schema_matched = False
            for schema_type in catalog:
                try:
                    for file_match in schema_type["fileMatch"]:
                        # Escape the fileMatch and perform a regex search
                         if(re.compile(file_match.replace("/","\/").replace(".","\.").replace("*",".*")).match(file_name)):
                            schema_url = schema_type['url']
                            schema_matched = True
                            break
                # Some schemas don't have a fileMatch attribute
                except LookupError as e:
                    pass
            if schema_matched == False:
                self.message = "No schema could be matched based on the file name. Try adding a $schema attribute to your file"
                self.result = False
                return
        # Use schema_url to retrieve schema
        try:
            request = urllib.request.Request(schema_url, headers={"User-Agent": "Sublime"})
            http_file = urllib.request.urlopen(request, timeout=5)
            http_response = http_file.read().decode('utf-8') 
            try:
                schema = json.loads(http_response)
            except ValueError as e:
                self.message = "Retrieved schema is not a valid JSON file"
                self.result = False
                return
        except (urllib.request.HTTPError) as e:
            self.message = "%s: HTTP error %s contacting API" % (__name__, str(e.code))
            self.result = False
            return
        except (urllib.request.URLError) as e:
            self.message = "%s: URL error %s contacting API" % (__name__, str(e.reason))
            return
            self.result = False
        try:
            jsonschema.validate(json_data, schema)
        except jsonschema.exceptions.ValidationError as e:
            self.message = "JSON schema validation failed | %s" % e.message
            self.result = False
            return
        except jsonschema.exceptions.SchemaError as e:
            self.message = "JSON schema validation failed | %s" % e.message
            self.result = False
            return
        self.message = "JSON Schema successfully validated against %s" % schema_url
        self.result = True
        return
