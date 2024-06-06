# Qiskit Code Assistant Jupyterlab Extension

[![Github Actions Status](https://github.ibm.com/IBM-Q-Software/qiskit-code-assistant-jupyterlab/workflows/Build/badge.svg)](https://github.ibm.com/IBM-Q-Software/qiskit-code-assistant-jupyterlab/actions/workflows/build.yml)

A JupyterLab extension for Qiskit Code Assistant

You can also use the [VSCode extension](https://github.ibm.com/IBM-Q-Software/qiskit-code-assistant-vscode)
if you dont have access to Jupyterlab

This extension is composed of a Python package named `qiskit_code_assistant_jupyterlab`
for the server extension and a NPM package named `qiskit-code-assistant-jupyterlab`
for the frontend extension.

## Requirements

- JupyterLab >= 4.0.0
- An instance of the [Qiskit Code Assistant Service](https://github.ibm.com/IBM-Q-Software/qiskit-code-assistant-service)

## Install

To install the extension, execute:

```bash
pip install qiskit_code_assistant_jupyterlab
```

To install the extension using a GitHub release, download the whl file from the [latest release](https://github.ibm.com/IBM-Q-Software/qiskit-code-assistant-jupyterlab/releases), then execute:

```bash
pip install PATH/TO/DOWNLOADED/FILE.whl
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall qiskit_code_assistant_jupyterlab
```

## Using the Qiskit Code Assistant

### IBM Quantum API Token

To make calls to the service API the extension requires an IBM Quantum API token.

#### Getting your API token

Open the [IBM Quantum website](https://quantum.ibm.com/) in your browser and login with your IBM Quantum account.
After logging in, an API token is displayed on the upper right side of the webpage.

![IBM Quantum API Key](docs/images/api-key.png)

#### Submitting your API token to the extension

When you first open Jupyterlab in a new window or tab you may see that the status bar
is highlighted orange, this shows that the service is not reachable.

![statusbar warning](docs/images/statusbar-no-model.png)

If you click the status bar or try to run the completer a dialog will display asking
for your API token, paste the token copied above here.

![token dialog](docs/images/enter-token.png)

You can also search for "Qiskit" in the command palette (`Alt Shift C`) to enter or
update your API token.

Once you've submitted a valid API key then the model select dialog will show, you can
open this dialog again to change models by clicking the statusbar.

![select a model](docs/images/select-model.png)

In addition if the enviroment variable `QISKIT_IBM_TOKEN` is set or the Qiskit
configuration file `~/.qiskit/qiskit-ibm.json` exists then the API token will be
populated at application start. If an API token is entered via the extension it will be
stored in `~/.qiskit/qiskit-ibm.json` under a new config named `qiskit-code-assistant`

### Using the Inline Completer

The inline completer can be triggered using the following key strokes.

- `Alt .` or `Alt \` will run the completer at the current cursor location
- `Alt [` and `Alt ]` can be used to cycle through the list of suggestions if there are
  more than one
- `Alt Tab` or `Alt END` will "accept" the suggested code and insert it at the current
  cursor location

In addition, once the completer runs you can use the buttons on the inline completer
widget to cycle or accept

![inline complete example](docs/images/inline-complete.png)

> NOTE: The service can sometime take a few seconds to retrun a suggestion, you can see
> when the service is working by checking the status bar

![working](docs/images/statusbar-working.png)

### Using the Code Completer

Jupyterlab also includes a traditional completer than displays suggestion in a context
menu rather than inline. This completer can be triggered using `Tab` to run and display
the context menu.

The context menu will include suggestions from the default completer in addition to the
Qiskit Code Assistant suggestions. The context menu also sanitizes and trims the
suggestions, making it less useful for see the code suggestion before inserting it.

![tab complete example](docs/images/tab-complete.png)

### Jupyterlab Settings

There are a few settings we recommend to edit in your user settings.

1. Inline Completer `showWidget` can be set to `always` in order to always show the
   inline completer widget to cycle through and select a completion item

2. Code Completion `providerTimeout` can be increased, our suggested value is `10000` or
   10 seconds. This is 1 second by default and the Qiskit Code Assistant API rarely returns
   within 1 second. This setting only apply the the standard completer that is invoked with
   `Tab`, the inline completer has a default of 10 seconds.

3. If you want to change the instance of the Qiskit Code Assistant Service that the
   extension should use you can edit the Qiskit Code Assistant setting `serviceUrl`

## Troubleshoot

If you are seeing the frontend extension, but it is not working, check that the server
extension is enabled:

```bash
jupyter server extension list
```

If the server extension is installed and enabled, but you are not seeing the frontend
extension, check the frontend extension is installed:

```bash
jupyter labextension list
```

## Contributing

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

```bash
# Clone the repo to your local environment
# Change directory to the qiskit_code_assistant_jupyterlab directory
# Install package in development mode
pip install -e "."
# Link your development version of the extension with JupyterLab
jupyter labextension develop . --overwrite
# Server extension must be manually installed in develop mode
jupyter server extension enable qiskit_code_assistant_jupyterlab
# Rebuild extension Typescript source after making changes
jlpm build
```

You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm watch
# Run JupyterLab in another terminal
jupyter lab
```

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

By default, the `jlpm build` command generates the source maps for this extension to make it easier to debug using the browser dev tools. To also generate source maps for the JupyterLab core extensions, you can run the following command:

```bash
jupyter lab build --minimize=False
```

### Development uninstall

```bash
# Server extension must be manually disabled in develop mode
jupyter server extension disable qiskit_code_assistant_jupyterlab
pip uninstall qiskit_code_assistant_jupyterlab
```

In development mode, you will also need to remove the symlink created by `jupyter labextension develop`
command. To find its location, you can run `jupyter labextension list` to figure out where the `labextensions`
folder is located. Then you can remove the symlink named `qiskit-code-assistant-jupyterlab` within that folder.

### Packaging the extension

See [RELEASE](RELEASE.md)
