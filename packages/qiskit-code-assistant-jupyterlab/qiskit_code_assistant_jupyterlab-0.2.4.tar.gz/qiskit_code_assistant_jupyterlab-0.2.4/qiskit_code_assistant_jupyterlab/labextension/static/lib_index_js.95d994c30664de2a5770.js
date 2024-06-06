"use strict";
(self["webpackChunkqiskit_code_assistant_jupyterlab"] = self["webpackChunkqiskit_code_assistant_jupyterlab"] || []).push([["lib_index_js"],{

/***/ "./lib/QiskitCompletionProvider.js":
/*!*****************************************!*\
  !*** ./lib/QiskitCompletionProvider.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   QiskitCompletionProvider: () => (/* binding */ QiskitCompletionProvider),
/* harmony export */   QiskitInlineCompletionProvider: () => (/* binding */ QiskitInlineCompletionProvider)
/* harmony export */ });
/* harmony import */ var _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/completer */ "webpack/sharing/consume/default/@jupyterlab/completer");
/* harmony import */ var _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _service_api__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./service/api */ "./lib/service/api.js");
/* harmony import */ var _service_autocomplete__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./service/autocomplete */ "./lib/service/autocomplete.js");
/* harmony import */ var _utils_icons__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./utils/icons */ "./lib/utils/icons.js");
/*
 * Copyright 2024 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */





function getInputText(text, widget) {
    const cellsContents = [];
    if (widget instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.NotebookPanel) {
        const currentCellIndex = widget.content.activeCellIndex;
        const cells = widget.content.widgets;
        for (let i = 0; i < currentCellIndex; i++) {
            if (cells[i].model.type === 'code') {
                const content = cells[i].model.toJSON().source;
                cellsContents.push(Array.isArray(content) ? content.join('\n') : content);
            }
        }
        cellsContents.push(text);
        return cellsContents.join('\n');
    }
    return text;
}
class QiskitCompletionProvider {
    constructor(options) {
        this.identifier = 'QiskitCodeAssistant:completer';
        this.rank = 1100;
        this.prompt_id = '';
        this.settings = options.settings;
    }
    async fetch(request, context) {
        const text = getInputText(request.text, context.widget);
        return (0,_service_autocomplete__WEBPACK_IMPORTED_MODULE_2__.autoComplete)(text).then(results => {
            this.prompt_id = results.prompt_id;
            return {
                start: request.offset,
                end: request.offset,
                items: results.items.map((item) => {
                    return {
                        label: item.trim(),
                        insertText: item,
                        icon: _utils_icons__WEBPACK_IMPORTED_MODULE_3__.qiskitIcon
                    };
                })
            };
        });
    }
    async isApplicable(context) {
        // Only fetch when enabled in settings
        return this.settings.composite['enableCompleter'];
    }
    accept() {
        if (this.prompt_id) {
            (0,_service_api__WEBPACK_IMPORTED_MODULE_4__.postModelPromptAccept)(this.prompt_id);
        }
    }
}
class QiskitInlineCompletionProvider {
    constructor() {
        this.icon = _utils_icons__WEBPACK_IMPORTED_MODULE_3__.qiskitIcon;
        this.identifier = 'qiskit-code-assistant-inline-completer';
        this.name = 'Qiskit Code Assistant';
        this.prompt_id = '';
        this.schema = {
            default: {
                enabled: true,
                timeout: 10000
            }
        };
    }
    async fetch(request, context) {
        if (context.triggerKind === _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0__.InlineCompletionTriggerKind.Automatic) {
            // Don't call the API when fetch is not manually triggered
            return { items: [] };
        }
        const text = getInputText(request.text, context.widget);
        return (0,_service_autocomplete__WEBPACK_IMPORTED_MODULE_2__.autoComplete)(text).then(results => {
            this.prompt_id = results.prompt_id;
            return {
                items: results.items.map((item) => {
                    return { insertText: item };
                })
            };
        });
    }
    async isApplicable(context) {
        // Always fetch, any filtering is handled by the service
        return true;
    }
    accept() {
        if (this.prompt_id) {
            (0,_service_api__WEBPACK_IMPORTED_MODULE_4__.postModelPromptAccept)(this.prompt_id);
        }
    }
}


/***/ }),

/***/ "./lib/StatusBarWidget.js":
/*!********************************!*\
  !*** ./lib/StatusBarWidget.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   StatusBarWidget: () => (/* binding */ StatusBarWidget)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _service_disclaimer__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./service/disclaimer */ "./lib/service/disclaimer.js");
/* harmony import */ var _service_modelHandler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./service/modelHandler */ "./lib/service/modelHandler.js");
/* harmony import */ var _service_token__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./service/token */ "./lib/service/token.js");
/*
 * Copyright 2024 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */






class StatusBarWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Widget {
    constructor() {
        super();
        const statusBar = document.createElement('div');
        statusBar.title = 'Click to change the model';
        statusBar.classList.add('jp-qiskit-code-assistant-statusbar');
        statusBar.classList.add('jp-StatusBar-GroupItem');
        this.addClass('jp-mod-highlighted');
        this.node.appendChild(statusBar);
        this._statusBar = statusBar;
        this.refreshStatusBar();
        StatusBarWidget.widget = this;
    }
    /**
     * Updates the statusbar
     */
    refreshStatusBar() {
        const curentModel = (0,_service_modelHandler__WEBPACK_IMPORTED_MODULE_3__.getCurrentModel)();
        if (curentModel) {
            this._statusBar.innerHTML =
                'Qiskit Code Assistant: ' + curentModel.display_name;
            this.removeClass('jp-qiskit-code-assistant-statusbar-warn');
        }
        else {
            this._statusBar.innerHTML = 'Qiskit Code Assistant: No Model Selected';
            this.addClass('jp-qiskit-code-assistant-statusbar-warn');
        }
    }
    setLoadingStatus() {
        this._statusBar.innerHTML = this._statusBar.innerHTML + _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.refreshIcon.svgstr;
    }
    async onClick() {
        await (0,_service_token__WEBPACK_IMPORTED_MODULE_4__.checkAPIToken)().then(() => {
            const modelsList = (0,_service_modelHandler__WEBPACK_IMPORTED_MODULE_3__.getModelsList)();
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getItem({
                title: 'Select a Model',
                items: [...modelsList.map(m => m.display_name)]
            }).then(result => {
                if (result.button.accept) {
                    const model = modelsList.find(m => m.display_name === result.value);
                    if (model) {
                        (0,_service_disclaimer__WEBPACK_IMPORTED_MODULE_5__.showDisclaimer)(model._id).then(accepted => {
                            if (accepted) {
                                (0,_service_modelHandler__WEBPACK_IMPORTED_MODULE_3__.setCurrentModel)(model);
                            }
                        });
                    }
                }
            });
        });
    }
    /**
     * Callback when the widget is added to the DOM
     */
    onAfterAttach(msg) {
        super.onAfterAttach(msg);
        this._statusBar.addEventListener('click', this.onClick.bind(this));
    }
    /**
     * Callback when the widget is removed from the DOM
     */
    onBeforeDetach(msg) {
        this._statusBar.removeEventListener('click', this.onClick.bind(this));
        super.onBeforeDetach(msg);
    }
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/completer */ "webpack/sharing/consume/default/@jupyterlab/completer");
/* harmony import */ var _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_completer__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _StatusBarWidget__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./StatusBarWidget */ "./lib/StatusBarWidget.js");
/* harmony import */ var _QiskitCompletionProvider__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./QiskitCompletionProvider */ "./lib/QiskitCompletionProvider.js");
/* harmony import */ var _service_api__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./service/api */ "./lib/service/api.js");
/* harmony import */ var _service_modelHandler__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./service/modelHandler */ "./lib/service/modelHandler.js");
/* harmony import */ var _service_token__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./service/token */ "./lib/service/token.js");
/*
 * Copyright 2024 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */









const EXTENSION_ID = 'qiskit-code-assistant-jupyterlab';
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.acceptInline = 'inline-completer:accept';
    CommandIDs.selectCompleterNotebook = 'completer:select-notebook';
    CommandIDs.selectCompleterFile = 'completer:select-file';
    CommandIDs.updateApiToken = 'qiskit-code-assistant:set-api-token';
})(CommandIDs || (CommandIDs = {}));
/**
 * Initialization data for the qiskit-code-assistant-jupyterlab extension.
 */
const plugin = {
    id: EXTENSION_ID + ':plugin',
    description: 'AI Autocomplete JupyterLab extension for Qiskit Code Assistant',
    autoStart: true,
    requires: [
        _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_1__.ICompletionProviderManager,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette,
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__.ISettingRegistry,
        _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_3__.IStatusBar
    ],
    activate: async (app, completionProviderManager, palette, settingRegistry, statusBar) => {
        console.debug('JupyterLab extension ' + EXTENSION_ID + ' is activated!');
        const settings = await settingRegistry.load(plugin.id);
        console.debug(EXTENSION_ID + ' settings loaded:', settings.composite);
        (0,_service_api__WEBPACK_IMPORTED_MODULE_4__.postServiceUrl)(settings.composite['serviceUrl']);
        settings.changed.connect(() => (0,_service_api__WEBPACK_IMPORTED_MODULE_4__.postServiceUrl)(settings.composite['serviceUrl']));
        const provider = new _QiskitCompletionProvider__WEBPACK_IMPORTED_MODULE_5__.QiskitCompletionProvider({ settings });
        const inlineProvider = new _QiskitCompletionProvider__WEBPACK_IMPORTED_MODULE_5__.QiskitInlineCompletionProvider();
        completionProviderManager.registerProvider(provider);
        completionProviderManager.registerInlineProvider(inlineProvider);
        const statusBarWidget = new _StatusBarWidget__WEBPACK_IMPORTED_MODULE_6__.StatusBarWidget();
        statusBar.registerStatusItem(EXTENSION_ID + ':statusbar', {
            item: statusBarWidget,
            align: 'left'
        });
        await (0,_service_modelHandler__WEBPACK_IMPORTED_MODULE_7__.refreshModelsList)().catch(reason => {
            console.error('Failed initial load of models list', reason);
        });
        app.commands.addCommand(CommandIDs.updateApiToken, {
            label: 'Qiskit Code Assistant: Set IBM Quantum API token',
            execute: () => (0,_service_token__WEBPACK_IMPORTED_MODULE_8__.updateAPIToken)()
        });
        palette.addItem({
            command: CommandIDs.updateApiToken,
            category: 'Qiskit Code Assistant'
        });
        app.commands.commandExecuted.connect((registry, executed) => {
            if (executed.id === CommandIDs.selectCompleterFile ||
                executed.id === CommandIDs.selectCompleterNotebook) {
                provider.accept();
            }
            else if (executed.id === CommandIDs.acceptInline) {
                inlineProvider.accept();
            }
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/service/api.js":
/*!****************************!*\
  !*** ./lib/service/api.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   getAPIToken: () => (/* binding */ getAPIToken),
/* harmony export */   getModel: () => (/* binding */ getModel),
/* harmony export */   getModelDisclaimer: () => (/* binding */ getModelDisclaimer),
/* harmony export */   getModels: () => (/* binding */ getModels),
/* harmony export */   postApiToken: () => (/* binding */ postApiToken),
/* harmony export */   postDisclaimerAccept: () => (/* binding */ postDisclaimerAccept),
/* harmony export */   postModelPrompt: () => (/* binding */ postModelPrompt),
/* harmony export */   postModelPromptAccept: () => (/* binding */ postModelPromptAccept),
/* harmony export */   postServiceUrl: () => (/* binding */ postServiceUrl)
/* harmony export */ });
/* harmony import */ var _utils_handler__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../utils/handler */ "./lib/utils/handler.js");
/*
 * Copyright 2024 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// POST /service
async function postServiceUrl(newUrl) {
    return await (0,_utils_handler__WEBPACK_IMPORTED_MODULE_0__.requestAPI)('service', {
        method: 'POST',
        body: JSON.stringify({ url: newUrl })
    }).then(response => {
        if (response.ok) {
            response.json().then(json => {
                console.debug('Updated service URL:', json.url);
            });
        }
        else {
            console.error('Error updating service URL', response.status, response.statusText);
            throw Error(response.statusText);
        }
    });
}
// GET /token
async function getAPIToken() {
    return await (0,_utils_handler__WEBPACK_IMPORTED_MODULE_0__.requestAPI)('token').then(async (response) => {
        if (response.ok) {
            const json = await response.json();
            return json['success'];
        }
        else {
            console.error('Error getting models', response.status, response.statusText);
            throw Error(response.statusText);
        }
    });
}
// POST /token
async function postApiToken(apiToken) {
    return await (0,_utils_handler__WEBPACK_IMPORTED_MODULE_0__.requestAPI)('token', {
        method: 'POST',
        body: JSON.stringify({ token: apiToken })
    }).then(response => {
        if (response.ok) {
            response.json().then(json => {
                console.debug('IBM Quantum API Token stored');
            });
        }
        else {
            console.error('Error submitting IBM Quantum API Token', response.status, response.statusText);
            throw Error(response.statusText);
        }
    });
}
// GET /models
async function getModels() {
    return await (0,_utils_handler__WEBPACK_IMPORTED_MODULE_0__.requestAPI)('models').then(async (response) => {
        if (response.ok) {
            const json = await response.json();
            console.debug('models list:', json);
            return json['models'];
        }
        else {
            console.error('Error getting models', response.status, response.statusText);
            throw Error(response.statusText);
        }
    });
}
// GET /model/{model_id}
async function getModel(model_id) {
    return await (0,_utils_handler__WEBPACK_IMPORTED_MODULE_0__.requestAPI)(`model/${model_id}`).then(async (response) => {
        if (response.ok) {
            const model = await response.json();
            console.debug('model:', model);
            return model;
        }
        else {
            console.error('Error getting model', response.status, response.statusText);
            throw Error(response.statusText);
        }
    });
}
// GET /model/{model_id}/disclaimer
async function getModelDisclaimer(model_id) {
    return await (0,_utils_handler__WEBPACK_IMPORTED_MODULE_0__.requestAPI)(`model/${model_id}/disclaimer`).then(async (response) => {
        if (response.ok) {
            return await response.json();
        }
        else {
            console.error('Error getting disclaimer', response.status, response.statusText);
            throw Error(response.statusText);
        }
    });
}
// POST /disclaimer/{disclaimer_id}/acceptance
async function postDisclaimerAccept(disclaimer_id, model) {
    return await (0,_utils_handler__WEBPACK_IMPORTED_MODULE_0__.requestAPI)(`disclaimer/${disclaimer_id}/acceptance`, {
        method: 'POST',
        body: JSON.stringify({ model, accepted: true })
    }).then(async (response) => {
        if (response.ok) {
            return await response.json();
        }
        else {
            console.error('Error accepting disclaimer', response.status, response.statusText);
            throw Error(response.statusText);
        }
    });
}
// POST /model/{model_id}/prompt
async function postModelPrompt(model_id, input) {
    return await (0,_utils_handler__WEBPACK_IMPORTED_MODULE_0__.requestAPI)(`model/${model_id}/prompt`, {
        method: 'POST',
        body: JSON.stringify({ input })
    }).then(async (response) => {
        if (response.ok) {
            const promptRes = await response.json();
            console.debug('prompt:', promptRes);
            return promptRes;
        }
        else {
            console.error('Error sending prompt', response.status, response.statusText);
            throw Error(response.statusText);
        }
    });
}
// POST /prompt/{prompt_id}/acceptance
async function postModelPromptAccept(prompt_id) {
    return await (0,_utils_handler__WEBPACK_IMPORTED_MODULE_0__.requestAPI)(`prompt/${prompt_id}/acceptance`, {
        method: 'POST',
        body: JSON.stringify({ accepted: true })
    }).then(async (response) => {
        if (response.ok) {
            return await response.json();
        }
        else {
            console.error('Error accepting prompt', response.status, response.statusText);
            throw Error(response.statusText);
        }
    });
}


/***/ }),

/***/ "./lib/service/autocomplete.js":
/*!*************************************!*\
  !*** ./lib/service/autocomplete.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   CHAR_LIMIT: () => (/* binding */ CHAR_LIMIT),
/* harmony export */   autoComplete: () => (/* binding */ autoComplete)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./api */ "./lib/service/api.js");
/* harmony import */ var _disclaimer__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./disclaimer */ "./lib/service/disclaimer.js");
/* harmony import */ var _modelHandler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./modelHandler */ "./lib/service/modelHandler.js");
/* harmony import */ var _token__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./token */ "./lib/service/token.js");
/* harmony import */ var _StatusBarWidget__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../StatusBarWidget */ "./lib/StatusBarWidget.js");
/*
 * Copyright 2024 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */





const CHAR_LIMIT = 4000;
async function promptPromise(model, requestText) {
    // Show loading icon in status bar
    _StatusBarWidget__WEBPACK_IMPORTED_MODULE_0__.StatusBarWidget.widget.setLoadingStatus();
    return (0,_api__WEBPACK_IMPORTED_MODULE_1__.postModelPrompt)(model, requestText).then((response) => {
        const items = [];
        response.results.map(results => items.push(results.generated_text));
        return {
            items,
            prompt_id: response.prompt_id
        };
    });
}
async function autoComplete(text) {
    const emptyReturn = { items: [], prompt_id: '' };
    return await (0,_token__WEBPACK_IMPORTED_MODULE_2__.checkAPIToken)()
        .then(async () => {
        const startingOffset = Math.max(0, text.length - CHAR_LIMIT);
        const requestText = text.slice(startingOffset, text.length);
        const model = (0,_modelHandler__WEBPACK_IMPORTED_MODULE_3__.getCurrentModel)();
        return await (0,_api__WEBPACK_IMPORTED_MODULE_1__.getModel)((model === null || model === void 0 ? void 0 : model._id) || '')
            .then(async (model) => {
            var _a;
            if ((_a = model.disclaimer) === null || _a === void 0 ? void 0 : _a.accepted) {
                return await promptPromise(model._id, requestText);
            }
            else {
                return await (0,_disclaimer__WEBPACK_IMPORTED_MODULE_4__.showDisclaimer)(model._id).then(async (accepted) => {
                    if (accepted) {
                        return await promptPromise(model._id, requestText);
                    }
                    else {
                        console.error('Disclaimer not accepted');
                        return emptyReturn;
                    }
                });
            }
        })
            .catch(reason => {
            console.error('Failed to send prompt', reason);
            return emptyReturn;
        });
    })
        .catch(reason => {
        console.error('Failed to send prompt', reason);
        return emptyReturn;
    })
        .finally(() => {
        // Remove loading icon from status bar
        _StatusBarWidget__WEBPACK_IMPORTED_MODULE_0__.StatusBarWidget.widget.refreshStatusBar();
    });
}


/***/ }),

/***/ "./lib/service/disclaimer.js":
/*!***********************************!*\
  !*** ./lib/service/disclaimer.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   showDisclaimer: () => (/* binding */ showDisclaimer)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./api */ "./lib/service/api.js");
/* harmony import */ var _modelHandler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./modelHandler */ "./lib/service/modelHandler.js");
/*
 * Copyright 2024 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */




async function showDisclaimer(model_id) {
    return await (0,_api__WEBPACK_IMPORTED_MODULE_2__.getModelDisclaimer)(model_id).then(async (disclaimerRes) => {
        if (disclaimerRes.accepted) {
            return disclaimerRes.accepted;
        }
        const bodyHtml = { __html: disclaimerRes.body };
        return await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
            title: disclaimerRes.title,
            body: react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { dangerouslySetInnerHTML: bodyHtml }),
            buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton(), _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton({ label: 'Accept' })]
        }).then(async (result) => {
            // Do nothing if the cancel button is pressed
            if (result.button.accept) {
                return await (0,_api__WEBPACK_IMPORTED_MODULE_2__.postDisclaimerAccept)(disclaimerRes._id, model_id).then(async (res) => {
                    return await (0,_modelHandler__WEBPACK_IMPORTED_MODULE_3__.refreshModelsList)().then(() => {
                        return res.success;
                    });
                });
            }
            else {
                return false;
            }
        });
    });
}


/***/ }),

/***/ "./lib/service/modelHandler.js":
/*!*************************************!*\
  !*** ./lib/service/modelHandler.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   getCurrentModel: () => (/* binding */ getCurrentModel),
/* harmony export */   getModelsList: () => (/* binding */ getModelsList),
/* harmony export */   refreshModelsList: () => (/* binding */ refreshModelsList),
/* harmony export */   setCurrentModel: () => (/* binding */ setCurrentModel)
/* harmony export */ });
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./api */ "./lib/service/api.js");
/* harmony import */ var _StatusBarWidget__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../StatusBarWidget */ "./lib/StatusBarWidget.js");
/*
 * Copyright 2024 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


let modelsList = [];
let currentModel = undefined;
function getModelsList() {
    return modelsList;
}
function getCurrentModel() {
    return currentModel;
}
function setCurrentModel(model) {
    var _a;
    currentModel = modelsList.find(m => m._id === (model === null || model === void 0 ? void 0 : model._id));
    (_a = _StatusBarWidget__WEBPACK_IMPORTED_MODULE_0__.StatusBarWidget.widget) === null || _a === void 0 ? void 0 : _a.refreshStatusBar();
}
async function refreshModelsList() {
    return await (0,_api__WEBPACK_IMPORTED_MODULE_1__.getModels)()
        .then(models => {
        var _a;
        modelsList = models;
        currentModel =
            modelsList.find(m => m._id === (currentModel === null || currentModel === void 0 ? void 0 : currentModel._id)) || (models === null || models === void 0 ? void 0 : models[0]);
        (_a = _StatusBarWidget__WEBPACK_IMPORTED_MODULE_0__.StatusBarWidget.widget) === null || _a === void 0 ? void 0 : _a.refreshStatusBar();
    })
        .catch(reason => {
        throw new Error(reason);
    });
}


/***/ }),

/***/ "./lib/service/token.js":
/*!******************************!*\
  !*** ./lib/service/token.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   checkAPIToken: () => (/* binding */ checkAPIToken),
/* harmony export */   updateAPIToken: () => (/* binding */ updateAPIToken)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./api */ "./lib/service/api.js");
/* harmony import */ var _modelHandler__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./modelHandler */ "./lib/service/modelHandler.js");
/*
 * Copyright 2024 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */



async function checkAPIToken() {
    const apiToken = await (0,_api__WEBPACK_IMPORTED_MODULE_1__.getAPIToken)();
    if (!apiToken) {
        return await updateAPIToken();
    }
}
async function updateAPIToken() {
    await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getPassword({
        title: 'Enter your API token from quantum.ibm.com',
        label: 'In order to use Qiskit Code Assistant you need a IBM Quantum API Token'
    })
        .then(async (result) => {
        if (result.button.accept && result.value) {
            return await (0,_api__WEBPACK_IMPORTED_MODULE_1__.postApiToken)(result.value).then(async () => {
                try {
                    return await (0,_modelHandler__WEBPACK_IMPORTED_MODULE_2__.refreshModelsList)();
                }
                catch (reason) {
                    console.error('Failed to load models list', reason);
                }
            });
        }
        else {
            throw Error('API token not set');
        }
    })
        .catch(() => {
        throw Error('API token not set');
    });
}


/***/ }),

/***/ "./lib/utils/handler.js":
/*!******************************!*\
  !*** ./lib/utils/handler.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   requestAPI: () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);
/*
 * Copyright 2024 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the requestd
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'qiskit-code-assistant', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        console.error('The qiskit_code_assistant_jupyterlab server extension appears to be missing.\n', error);
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    return response;
}


/***/ }),

/***/ "./lib/utils/icons.js":
/*!****************************!*\
  !*** ./lib/utils/icons.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   qiskitIcon: () => (/* binding */ qiskitIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _style_icons_Qiskit_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../style/icons/Qiskit.svg */ "./style/icons/Qiskit.svg");
/*
 * Copyright 2024 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


const qiskitIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'qiskit:logo',
    svgstr: _style_icons_Qiskit_svg__WEBPACK_IMPORTED_MODULE_1__
});


/***/ }),

/***/ "./style/icons/Qiskit.svg":
/*!********************************!*\
  !*** ./style/icons/Qiskit.svg ***!
  \********************************/
/***/ ((module) => {

module.exports = "<svg id=\"qiskit\" xmlns=\"http://www.w3.org/2000/svg\" width=\"24px\" height=\"24px\" viewBox=\"0 0 200 200\">\n    <path fill=\"#fff\" d=\"M174.09,100.19c0-.07,0-.14,0-.22s0-.44,0-.67a74.13,74.13,0,0,0-15-44,12.85,12.85,0,0,0-3.37-4.11A74.34,74.34,0,0,0,102.42,26c-.8,0-1.61-.08-2.42-.08s-1.41,0-2.11.06A74,74,0,0,0,44.23,51.21a12.68,12.68,0,0,0-3.42,4.24A74.53,74.53,0,0,0,25.91,99.7a2.45,2.45,0,0,0,0,.27c0,.13,0,.25,0,.37A73.93,73.93,0,0,0,41.12,145a11.89,11.89,0,0,0,2.3,2.88,74.38,74.38,0,0,0,54.51,26.19c.69,0,1.38.05,2.07.05s1.27,0,1.91,0a74,74,0,0,0,54.88-26.49,12.65,12.65,0,0,0,2-2.51A74.64,74.64,0,0,0,174.09,100.19Zm-20.54,44.66c-3.56,3.23-11.35,6.54-22.6,8.83a6.47,6.47,0,0,0-5.68-3.35l-.51,0L114.07,126a128.16,128.16,0,0,1,24.71,4.12c10.45,3,16.95,7.17,16.95,11a3.66,3.66,0,0,1-.44,1.62C154.73,143.4,154.15,144.13,153.55,144.85Zm-54.9,11.78c-25.6-.27-45-5.52-51.76-11.25-.77-.91-1.53-1.84-2.27-2.8a3.91,3.91,0,0,1-.35-1.53c0-3.3,5.24-8.11,19.94-11.74a152.92,152.92,0,0,1,34-3.85H100c3.14,0,6.25.08,9.3.23l11.57,26.38a6.48,6.48,0,0,0-2,3.49A181.25,181.25,0,0,1,98.65,156.63Zm-1.18,13.16c-7.52-.48-12-3-12-4.38S91,161,100,161s14.56,2.89,14.56,4.46-4.66,4-12.39,4.4C100.6,169.85,99,169.85,97.47,169.79ZM47.37,54.07c4-3.1,11.52-6,21.71-8a7,7,0,0,0,6.22,3.8,5.85,5.85,0,0,0,.73,0L86.62,74C61.15,72,44.27,65.06,44.27,58.89a4,4,0,0,1,.24-1.3C45.43,56.39,46.37,55.21,47.37,54.07ZM100,43.29c25.78,0,45.41,5.07,52.67,10.82,1,1.1,1.9,2.25,2.8,3.42a3.9,3.9,0,0,1,.26,1.36c0,6.51-21.73,15.59-57.08,15.59-2.49,0-4.91-.1-7.27-.22L79.91,48.11a7,7,0,0,0,2.26-4C87.68,43.6,93.65,43.29,100,43.29Zm-14.56-8.7c0-1.47,4.85-4.1,12.9-4.42l1.54,0c.65,0,1.29,0,1.94,0,8,.35,12.74,3,12.74,4.41S109,39.05,100,39.05,85.44,36.17,85.44,34.59Zm50.43,47.27c20.23,3.84,33.44,10.74,34,17.68,0,.2,0,.4,0,.59-.27,8.9-23.45,18.63-58,20.69l-18.41-42q3.28-.1,6.61-.11A195.75,195.75,0,0,1,135.87,81.86ZM71.59,76.35q-4.26.59-8.28,1.35h0c-15.25,2.9-26.5,7.44-32.49,12.87A70.51,70.51,0,0,1,41,62.63C44.42,69.11,56.6,73.76,71.59,76.35ZM30.15,99.76c.26-7,13.53-14,33.95-17.89h0A186.59,186.59,0,0,1,88.84,79l18.43,42c-2.92.11-5.9.18-9,.18-40.45-.46-67.71-11.18-68.15-21C30.16,100.07,30.15,99.91,30.15,99.76ZM139.94,126a110.87,110.87,0,0,0-11.74-2.6,142.17,142.17,0,0,0,22.48-4.9c8.4-2.64,14.61-5.76,18.52-9.24a70.22,70.22,0,0,1-10.17,28C156.75,132.82,150.27,129,139.94,126Zm29.28-35.41c-6-5.46-17.26-10-32.55-12.92q-4.15-.78-8.57-1.38C143.38,73.67,155.57,69,159,62.57c.91,1.43,1.77,2.89,2.58,4.4A69.53,69.53,0,0,1,169.22,90.61Zm-53.7-50.9A6.4,6.4,0,0,0,118.76,35a2.12,2.12,0,0,0,0-.44,2,2,0,0,0,0-.43,5.19,5.19,0,0,0-.36-1.52A70.09,70.09,0,0,1,142.68,44.7,127.08,127.08,0,0,0,115.52,39.71ZM67,38.43A70.14,70.14,0,0,1,81.62,32.6a4.82,4.82,0,0,0-.38,1.56,2,2,0,0,0,0,.43,2.12,2.12,0,0,0,0,.44,6.43,6.43,0,0,0,3.24,4.68L81.66,40a7,7,0,0,0-13.28,1.93,94.18,94.18,0,0,0-11,2.79A70,70,0,0,1,67,38.43Zm-36.2,70.9c3.71,3.34,9.49,6.35,17.25,8.91a136.36,136.36,0,0,0,23.4,5.24c-2.86.49-5.61,1.06-8.22,1.71h0c-12,3-19.68,7.2-22.22,12.14-.89-1.4-1.74-2.82-2.54-4.3A69.65,69.65,0,0,1,30.77,109.33Zm53.86,50.85c-2,1.27-3.22,2.87-3.39,4.8a2,2,0,0,0,0,.43,2.12,2.12,0,0,0,0,.44,5,5,0,0,0,.35,1.49A70.2,70.2,0,0,1,56.9,155,127.31,127.31,0,0,0,84.63,160.18Zm48.4,1.39a69.81,69.81,0,0,1-14.64,5.82,5.1,5.1,0,0,0,.37-1.54,2.12,2.12,0,0,0,0-.44,2,2,0,0,0,0-.43c-.17-2-1.45-3.58-3.48-4.85,1.41-.13,2.8-.28,4.19-.44a6.48,6.48,0,0,0,12.21-1.9,98,98,0,0,0,11.72-3.06A69.92,69.92,0,0,1,133,161.57Z\"/>\n</svg>";

/***/ })

}]);
//# sourceMappingURL=lib_index_js.95d994c30664de2a5770.js.map