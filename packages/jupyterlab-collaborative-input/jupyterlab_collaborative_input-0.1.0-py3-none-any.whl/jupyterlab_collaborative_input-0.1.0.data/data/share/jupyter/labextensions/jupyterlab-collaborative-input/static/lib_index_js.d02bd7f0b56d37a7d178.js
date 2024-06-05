"use strict";
(self["webpackChunkjupyterlab_collaborative_input"] = self["webpackChunkjupyterlab_collaborative_input"] || []).push([["lib_index_js"],{

/***/ "./lib/collaborativeInputWidget.js":
/*!*****************************************!*\
  !*** ./lib/collaborativeInputWidget.js ***!
  \*****************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.PLUGIN_NAME = void 0;
const Y = __importStar(__webpack_require__(/*! yjs */ "webpack/sharing/consume/default/yjs"));
const widgets_1 = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
const outputarea_1 = __webpack_require__(/*! @jupyterlab/outputarea */ "webpack/sharing/consume/default/@jupyterlab/outputarea");
const codemirror_1 = __webpack_require__(/*! @jupyterlab/codemirror */ "webpack/sharing/consume/default/@jupyterlab/codemirror");
const view_1 = __webpack_require__(/*! @codemirror/view */ "webpack/sharing/consume/default/@codemirror/view");
const OUTPUT_AREA_ITEM_CLASS = 'jp-OutputArea-child';
const OUTPUT_AREA_STDIN_ITEM_CLASS = 'jp-OutputArea-stdin-item';
const OUTPUT_AREA_PROMPT_CLASS = 'jp-OutputArea-prompt';
const OUTPUT_AREA_OUTPUT_CLASS = 'jp-OutputArea-output';
const STDIN_CLASS = 'jp-Stdin';
const STDIN_PROMPT_CLASS = 'jp-Stdin-prompt';
const STDIN_INPUT_CLASS = 'jp-Stdin-input';
exports.PLUGIN_NAME = 'jupyterlab-collaborative-input';
class CollaborativeInputWidget extends widgets_1.Widget {
    constructor(panel, tracker) {
        super();
        this._panel = panel;
        //this._tracker = tracker;
        const cells = panel.context.model.cells;
        cells.changed.connect(this.updateConnectedCell, this);
    }
    updateConnectedCell(sender, changed) {
        //changed.oldValues.forEach(this._unobserveStdinOutput.bind(this));
        changed.newValues.forEach(this._observeStdinOutput.bind(this));
    }
    _observeStdinOutput(cellModel) {
        const codeCell = this._getCodeCell(cellModel);
        cellModel.sharedModel.changed.connect((sender, args) => { this.handleStdin(codeCell, args); });
        const youtputs = cellModel.sharedModel.ymodel.get('outputs');
        for (const youtput of youtputs) {
            if (youtput instanceof Y.Map && youtput.get('output_type') === 'stdin') {
                const prompt = youtput.get('prompt');
                const password = youtput.get('password');
                this.createInputWidget(codeCell, prompt, password, youtput);
            }
        }
    }
    handleStdin(sender, args) {
        if (args.outputsChange !== undefined &&
            args.outputsChange[0].insert !== undefined) {
            const newOutput = args.outputsChange[0].insert[0];
            const output_type = newOutput.get('output_type');
            if (output_type === 'stdin') {
                const prompt = newOutput.get('prompt');
                const password = newOutput.get('password');
                this.createInputWidget(sender, prompt, password, newOutput);
            }
        }
    }
    createInputWidget(cellModel, prompt, password, stdinOutput) {
        const inputWidget = new InputWidget(prompt, password, stdinOutput, cellModel.model.sharedModel.awareness);
        const panel = new widgets_1.Panel();
        panel.addClass(OUTPUT_AREA_ITEM_CLASS);
        panel.addClass(OUTPUT_AREA_STDIN_ITEM_CLASS);
        const outputPrompt = new outputarea_1.OutputPrompt();
        outputPrompt.addClass(OUTPUT_AREA_PROMPT_CLASS);
        panel.addWidget(outputPrompt);
        inputWidget.addClass(OUTPUT_AREA_OUTPUT_CLASS);
        panel.addWidget(inputWidget);
        cellModel.outputArea.layout.addWidget(panel);
    }
    _getCodeCell(cellModel) {
        if (cellModel.type === 'code') {
            const cell = this._panel.content.widgets.find((widget) => widget.model === cellModel);
            return cell;
        }
        return null;
    }
}
exports["default"] = CollaborativeInputWidget;
class InputWidget extends widgets_1.Widget {
    constructor(prompt, password, stdinOutput, awareness) {
        const node = document.createElement('div');
        const promptNode = document.createElement('pre');
        promptNode.className = STDIN_PROMPT_CLASS;
        promptNode.textContent = prompt;
        const input1 = document.createElement('div');
        input1.className = STDIN_INPUT_CLASS;
        input1.style.border = 'thin solid';
        const input2 = document.createElement('div');
        if (password === true) {
            input2.style.webkitTextSecurity = 'disc';
        }
        input1.appendChild(input2);
        node.appendChild(promptNode);
        promptNode.appendChild(input1);
        const stdin = stdinOutput.get('value');
        const ybind = (0, codemirror_1.ybinding)({ ytext: stdin });
        const submit = ({ state, dispatch }) => {
            stdinOutput.set('submitted', true);
            return true;
        };
        const submitWithEnter = {
            key: 'Enter',
            run: submit
        };
        new view_1.EditorView({
            doc: stdin.toString(),
            extensions: [view_1.keymap.of([submitWithEnter]), ybind],
            parent: input2
        });
        super({ node });
        this.addClass(STDIN_CLASS);
    }
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
const notebook_1 = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
const settingregistry_1 = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
const collaborativeInputWidget_1 = __importStar(__webpack_require__(/*! ./collaborativeInputWidget */ "./lib/collaborativeInputWidget.js"));
class CollaborativeInputWidgetExtension {
    constructor(tracker) {
        this._tracker = tracker;
    }
    createNew(panel, context) {
        return new collaborativeInputWidget_1.default(panel, this._tracker);
    }
}
const extension = {
    id: collaborativeInputWidget_1.PLUGIN_NAME,
    autoStart: true,
    requires: [notebook_1.INotebookTracker, settingregistry_1.ISettingRegistry],
    activate: async (app, tracker, settingRegistry) => {
        app.docRegistry.addWidgetExtension('Notebook', new CollaborativeInputWidgetExtension(tracker));
        // eslint-disable-next-line no-console
        console.log(`JupyterLab extension ${collaborativeInputWidget_1.PLUGIN_NAME} is activated!`);
    },
};
exports["default"] = extension;


/***/ })

}]);
//# sourceMappingURL=lib_index_js.d02bd7f0b56d37a7d178.js.map