# Sublime Schema Validator

A Sublime Text 3 extension for validating JSON Schemas

## Features

This plugin validates your JSON file using the schema pointed to by the `$schema` attribute.

If no `$schema` attribute exists, it will try and validate your schema using the file name

## Install

### Install via the amazing [Package Control Plugin](https://sublime.wbond.net/)

* Bring up the Command Palette (Cmd + Shift + P on OS X, Ctrl + Shift + P on Windows).
* Select `Package Control: Install Package`
* Select `Schema Validator` when the list appears.
* Package Control will automatically keep Schema Validator up to date with the latest version.

### Manual Install

Clone this repo to your Packages directory

    git clone http://github.com/shirhatti/SchemaValidator.git

On Mac this directory is located at `/Users/{user}/Library/Application\ Support/Sublime\ Text\ 3/Packages`.
On Windows this directory is located at `C:\Users\{user}\AppData\Roaming\Sublime Text 3\Packages`

## License

Copyright 2014 Sourabh Shirhatti

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


## Credits

#### [JSON Schema Store](https://github.com/madskristensen/schemastore)

Copyright 2014 Mads Kristensen

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

#### [jsonschema](https://github.com/Julian/jsonschema)

Copyright (c) 2013 Julian Berman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.