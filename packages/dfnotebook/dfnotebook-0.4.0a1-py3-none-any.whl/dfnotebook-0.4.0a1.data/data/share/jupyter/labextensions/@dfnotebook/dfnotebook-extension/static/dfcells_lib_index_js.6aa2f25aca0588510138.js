"use strict";
(self["webpackChunk_dfnotebook_dfnotebook_extension"] = self["webpackChunk_dfnotebook_dfnotebook_extension"] || []).push([["dfcells_lib_index_js"],{

/***/ "../dfcells/lib/index.js":
/*!*******************************!*\
  !*** ../dfcells/lib/index.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   DataflowAttachmentsCell: () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.DataflowAttachmentsCell),
/* harmony export */   DataflowCell: () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.DataflowCell),
/* harmony export */   DataflowCodeCell: () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.DataflowCodeCell),
/* harmony export */   DataflowInputArea: () => (/* reexport safe */ _inputarea__WEBPACK_IMPORTED_MODULE_0__.DataflowInputArea),
/* harmony export */   DataflowInputPrompt: () => (/* reexport safe */ _inputarea__WEBPACK_IMPORTED_MODULE_0__.DataflowInputPrompt),
/* harmony export */   DataflowMarkdownCell: () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.DataflowMarkdownCell),
/* harmony export */   DataflowRawCell: () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.DataflowRawCell)
/* harmony export */ });
/* harmony import */ var _inputarea__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./inputarea */ "../dfcells/lib/inputarea.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./widget */ "../dfcells/lib/widget.js");
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module dfcells
 */




/***/ }),

/***/ "../dfcells/lib/inputarea.js":
/*!***********************************!*\
  !*** ../dfcells/lib/inputarea.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   DataflowInputArea: () => (/* binding */ DataflowInputArea),
/* harmony export */   DataflowInputPrompt: () => (/* binding */ DataflowInputPrompt)
/* harmony export */ });
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/cells */ "webpack/sharing/consume/default/@jupyterlab/cells");
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__);

class DataflowInputArea extends _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.InputArea {
    // kind of annoying as model still needs to be set later
    constructor(options) {
        super(options);
        this.prompt.model = this.model;
    }
    get prompt() {
        //@ts-ignore
        return this._prompt;
    }
    set prompt(value) {
        value.model = this.model;
        //@ts-ignore
        this._prompt = value;
    }
    addTag(value) {
        var _a;
        (_a = this.model) === null || _a === void 0 ? void 0 : _a.setMetadata('tag', value);
        this.prompt.updatePromptNode(this.prompt.executionCount);
    }
}
(function (DataflowInputArea) {
    class ContentFactory extends _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.InputArea.ContentFactory {
        /**
         * Create an input prompt.
         */
        createInputPrompt() {
            return new DataflowInputPrompt();
        }
    }
    DataflowInputArea.ContentFactory = ContentFactory;
})(DataflowInputArea || (DataflowInputArea = {}));
class DataflowInputPrompt extends _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.InputPrompt {
    constructor(model = null) {
        super();
        this.model = model;
    }
    updatePromptNode(value) {
        var _a;
        if ((_a = this.model) === null || _a === void 0 ? void 0 : _a.getMetadata('tag')) {
            this.node.textContent = `[${this.model.getMetadata('tag')}]:`;
        }
        else if (value === null) {
            this.node.textContent = ' ';
        }
        else {
            this.node.textContent = `[${value || ' '}]:`;
        }
    }
    /**
     * The execution count for the prompt.
     */
    get executionCount() {
        return super.executionCount;
    }
    set executionCount(value) {
        super.executionCount = value;
        this.updatePromptNode(value);
    }
    get model() {
        return this._model;
    }
    set model(value) {
        this._model = value;
        if (this._model) {
            this.updatePromptNode(this.executionCount);
        }
    }
}


/***/ }),

/***/ "../dfcells/lib/widget.js":
/*!********************************!*\
  !*** ../dfcells/lib/widget.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   DataflowAttachmentsCell: () => (/* binding */ DataflowAttachmentsCell),
/* harmony export */   DataflowCell: () => (/* binding */ DataflowCell),
/* harmony export */   DataflowCodeCell: () => (/* binding */ DataflowCodeCell),
/* harmony export */   DataflowMarkdownCell: () => (/* binding */ DataflowMarkdownCell),
/* harmony export */   DataflowRawCell: () => (/* binding */ DataflowRawCell)
/* harmony export */ });
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/cells */ "webpack/sharing/consume/default/@jupyterlab/cells");
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _inputarea__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./inputarea */ "../dfcells/lib/inputarea.js");
/* harmony import */ var _dfnotebook_dfoutputarea__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @dfnotebook/dfoutputarea */ "../dfoutputarea/lib/widget.js");
/* harmony import */ var _dfnotebook_dfgraph__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @dfnotebook/dfgraph */ "../dfgraph/lib/dfgraph.js");



// FIXME need to add this back when dfgraph is working

/**
 * The CSS class added to the cell input area.
 */
const CELL_INPUT_AREA_CLASS = 'jp-Cell-inputArea';
/**
 * The CSS class added to the cell output area.
 */
const CELL_OUTPUT_AREA_CLASS = 'jp-Cell-outputArea';
function setInputArea(cell) {
    // FIXME may be able to get panel via (this.layout as PanelLayout).widgets?
    //@ts-expect-error
    const inputWrapper = cell._inputWrapper;
    const input = cell.inputArea;
    // find the input area widget
    let inputIdx = -1;
    if (input) {
        const { id } = input;
        inputWrapper.widgets.forEach((widget, idx) => {
            if (widget.id === id) {
                inputIdx = idx;
            }
        });
    }
    const dfInput = new _inputarea__WEBPACK_IMPORTED_MODULE_1__.DataflowInputArea({
        model: cell.model,
        contentFactory: cell.contentFactory,
        editorOptions: { config: cell.editorConfig }
    });
    dfInput.addClass(CELL_INPUT_AREA_CLASS);
    inputWrapper.insertWidget(inputIdx, dfInput);
    input === null || input === void 0 ? void 0 : input.dispose();
    //@ts-expect-error
    cell._input = dfInput;
}
function setOutputArea(cell) {
    //@ts-expect-error
    const outputWrapper = cell._outputWrapper;
    const output = cell.outputArea;
    // find the output area widget
    const { id } = output;
    let outputIdx = -1;
    outputWrapper.widgets.forEach((widget, idx) => {
        if (widget.id === id) {
            outputIdx = idx;
        }
    });
    const dfOutput = new _dfnotebook_dfoutputarea__WEBPACK_IMPORTED_MODULE_2__.DataflowOutputArea({
        model: cell.model.outputs,
        rendermime: output.rendermime,
        contentFactory: cell.contentFactory,
        maxNumberOutputs: output.maxNumberOutputs,
        //@ts-expect-error
        translator: output._translator,
        promptOverlay: true,
        //@ts-expect-error
        inputHistoryScope: output._inputHistoryScope
    }, 
    // FIXME move this to a function to unify with the code below and in dfnotebook/actions.tsx
    cell.model.id.replace(/-/g, '').substring(0, 8));
    dfOutput.addClass(CELL_OUTPUT_AREA_CLASS);
    output.toggleScrolling.disconnect(() => {
        cell.outputsScrolled = !cell.outputsScrolled;
    });
    dfOutput.toggleScrolling.connect(() => {
        cell.outputsScrolled = !cell.outputsScrolled;
    });
    // output.initialize.disconnect();
    // dfOutput.initialize.connect(() => {
    //   this.updatePromptOverlayIcon();
    // });
    output.outputLengthChanged.disconnect(
    //@ts-expect-error
    cell._outputLengthHandler, cell);
    //@ts-expect-error
    dfOutput.outputLengthChanged.connect(cell._outputLengthHandler, cell);
    outputWrapper.insertWidget(outputIdx, dfOutput);
    output.dispose();
    //@ts-expect-error
    cell._output = dfOutput;
}
class DataflowCell extends _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.Cell {
    initializeDOM() {
        super.initializeDOM();
        setInputArea(this);
        this.addClass('df-cell');
    }
}
(function (DataflowCell) {
    class ContentFactory extends _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.Cell.ContentFactory {
        /**
         * Create an input prompt.
         */
        createInputPrompt() {
            return new _inputarea__WEBPACK_IMPORTED_MODULE_1__.DataflowInputPrompt();
        }
        /**
         * Create the output prompt for the widget.
         */
        createOutputPrompt() {
            return new _dfnotebook_dfoutputarea__WEBPACK_IMPORTED_MODULE_2__.DataflowOutputPrompt();
        }
    }
    DataflowCell.ContentFactory = ContentFactory;
})(DataflowCell || (DataflowCell = {}));
class DataflowMarkdownCell extends _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.MarkdownCell {
    initializeDOM() {
        super.initializeDOM();
        setInputArea(this);
        this.addClass('df-cell');
    }
}
class DataflowRawCell extends _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.RawCell {
    initializeDOM() {
        super.initializeDOM();
        setInputArea(this);
        this.addClass('df-cell');
    }
}
class DataflowAttachmentsCell extends _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.AttachmentsCell {
    initializeDOM() {
        super.initializeDOM();
        setInputArea(this);
        this.addClass('df-cell');
    }
}
class DataflowCodeCell extends _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.CodeCell {
    initializeDOM() {
        super.initializeDOM();
        setInputArea(this);
        setOutputArea(this);
        this.setPromptToId();
        this.addClass('df-cell');
    }
    setPromptToId() {
        // FIXME move this to a function to unify with the code in dfnotebook/actions.tsx
        this.setPrompt(`${this.model.id.replace(/-/g, '').substring(0, 8) || ''}`);
    }
    initializeState() {
        super.initializeState();
        this.setPromptToId();
        return this;
    }
    onStateChanged(model, args) {
        super.onStateChanged(model, args);
        switch (args.name) {
            case 'executionCount':
                this.setPromptToId();
                break;
            default:
                break;
        }
    }
}
(function (DataflowCodeCell) {
    /**
     * Execute a cell given a client session.
     */
    async function execute(cell, sessionContext, metadata, dfData, cellIdModelMap) {
        var _a;
        const model = cell.model;
        const code = model.sharedModel.getSource();
        if (!code.trim() || !((_a = sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel)) {
            model.sharedModel.transact(() => {
                model.clearExecution();
            }, false);
            return;
        }
        const cellId = { cellId: model.sharedModel.getId() };
        metadata = {
            ...model.metadata,
            ...metadata,
            ...cellId
        };
        const { recordTiming } = metadata;
        model.sharedModel.transact(() => {
            model.clearExecution();
            cell.outputHidden = false;
        }, false);
        cell.setPrompt('*');
        model.trusted = true;
        let future;
        try {
            const cellIdOutputsMap = {};
            if (cellIdModelMap) {
                for (const cellId in cellIdModelMap) {
                    cellIdOutputsMap[cellId] = cellIdModelMap[cellId].outputs;
                }
            }
            const msgPromise = _dfnotebook_dfoutputarea__WEBPACK_IMPORTED_MODULE_2__.DataflowOutputArea.execute(code, cell.outputArea, sessionContext, metadata, dfData, cellIdOutputsMap);
            // cell.outputArea.future assigned synchronously in `execute`
            if (recordTiming) {
                const recordTimingHook = (msg) => {
                    let label;
                    switch (msg.header.msg_type) {
                        case 'status':
                            label = `status.${msg.content.execution_state}`;
                            break;
                        case 'execute_input':
                            label = 'execute_input';
                            break;
                        default:
                            return true;
                    }
                    // If the data is missing, estimate it to now
                    // Date was added in 5.1: https://jupyter-client.readthedocs.io/en/stable/messaging.html#message-header
                    const value = msg.header.date || new Date().toISOString();
                    const timingInfo = Object.assign({}, model.getMetadata('execution'));
                    timingInfo[`iopub.${label}`] = value;
                    model.setMetadata('execution', timingInfo);
                    return true;
                };
                cell.outputArea.future.registerMessageHook(recordTimingHook);
            }
            else {
                model.deleteMetadata('execution');
            }
            const clearOutput = (msg) => {
                switch (msg.header.msg_type) {
                    case 'execute_input':
                        const executionCount = msg
                            .content.execution_count;
                        if (executionCount !== null) {
                            const cellId = executionCount.toString(16).padStart(8, '0');
                            if (cellIdModelMap) {
                                const cellModel = cellIdModelMap[cellId];
                                cellModel.sharedModel.setSource(msg.content.code);
                                cellModel.outputs.clear();
                            }
                        }
                        break;
                    default:
                        return true;
                }
                return true;
            };
            cell.outputArea.future.registerMessageHook(clearOutput);
            // Save this execution's future so we can compare in the catch below.
            future = cell.outputArea.future;
            const msg = (await msgPromise);
            model.executionCount = msg.content.execution_count;
            if (recordTiming) {
                const timingInfo = Object.assign({}, model.getMetadata('execution'));
                const started = msg.metadata.started;
                // Started is not in the API, but metadata IPyKernel sends
                if (started) {
                    timingInfo['shell.execute_reply.started'] = started;
                }
                // Per above, the 5.0 spec does not assume date, so we estimate is required
                const finished = msg.header.date;
                timingInfo['shell.execute_reply'] =
                    finished || new Date().toISOString();
                model.setMetadata('execution', timingInfo);
            }
            let content = msg.content;
            let nodes = content.nodes;
            let uplinks = content.links;
            let cells = content.cells;
            let downlinks = content.imm_downstream_deps;
            let allUps = content.upstream_deps;
            let internalNodes = content.internal_nodes;
            let sessId = sessionContext.session.id;
            //Set information about the graph based on sessionid
            _dfnotebook_dfgraph__WEBPACK_IMPORTED_MODULE_3__.Manager.graphs[sessId].updateCellContents(dfData === null || dfData === void 0 ? void 0 : dfData.code_dict);
            _dfnotebook_dfgraph__WEBPACK_IMPORTED_MODULE_3__.Manager.graphs[sessId].updateGraph(cells, nodes, uplinks, downlinks, `${cell.model.id.substr(0, 8) || ''}`, allUps, internalNodes);
            _dfnotebook_dfgraph__WEBPACK_IMPORTED_MODULE_3__.Manager.updateDepViews(false);
            if (content.update_downstreams) {
                _dfnotebook_dfgraph__WEBPACK_IMPORTED_MODULE_3__.Manager.graphs[sessId].updateDownLinks(content.update_downstreams);
            }
            return msg;
        }
        catch (e) {
            // If we started executing, and the cell is still indicating this
            // execution, clear the prompt.
            if (future && !cell.isDisposed && cell.outputArea.future === future) {
                // cell.setPrompt('');
                // FIXME is this necessary?
                cell.setPromptToId();
                // cell.setPrompt(`${cell.model.id.substring(0, 8) || ''}`);
            }
            throw e;
        }
    }
    DataflowCodeCell.execute = execute;
})(DataflowCodeCell || (DataflowCodeCell = {}));


/***/ }),

/***/ "../dfoutputarea/lib/widget.js":
/*!*************************************!*\
  !*** ../dfoutputarea/lib/widget.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   DataflowOutputArea: () => (/* binding */ DataflowOutputArea),
/* harmony export */   DataflowOutputPrompt: () => (/* binding */ DataflowOutputPrompt)
/* harmony export */ });
/* harmony import */ var _jupyterlab_outputarea__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/outputarea */ "webpack/sharing/consume/default/@jupyterlab/outputarea");
/* harmony import */ var _jupyterlab_outputarea__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_outputarea__WEBPACK_IMPORTED_MODULE_0__);

class DataflowOutputArea extends _jupyterlab_outputarea__WEBPACK_IMPORTED_MODULE_0__.OutputArea {
    constructor(options, cellId) {
        super({
            contentFactory: DataflowOutputArea.defaultContentFactory,
            ...options
        });
        this.onIOPub = (msg) => {
            const model = this.model;
            const msgType = msg.header.msg_type;
            let execCountMsg;
            let output;
            const transient = (msg.content.transient || {});
            const displayId = transient['display_id'];
            let targets;
            switch (msgType) {
                case 'execute_result':
                    execCountMsg = msg;
                case 'display_data':
                    execCountMsg = msg;
                case 'stream':
                    execCountMsg = msg;
                case 'error':
                    execCountMsg = msg;
                    if (execCountMsg.content.execution_count) {
                        const cellId = execCountMsg.content.execution_count.toString(16).padStart(8, '0');
                        if (msgType === 'stream' || msgType === 'error') {
                            delete execCountMsg.content.execution_count;
                        }
                        output = { ...execCountMsg.content, output_type: msgType };
                        if (cellId != this.cellId) {
                            if (DataflowOutputArea.cellIdModelMap) {
                                const cellModel = DataflowOutputArea.cellIdModelMap[cellId];
                                cellModel.add(output);
                            }
                        }
                        else {
                            model.add(output);
                        }
                    }
                    else {
                        output = { ...execCountMsg.content, output_type: msgType };
                        model.add(output);
                    }
                    // FIXME do we have to do the displayId && msgType === 'display_data' stuff?
                    // is this only for update-display-data?
                    if (displayId && msgType === 'display_data') {
                        //@ts-expect-error
                        targets = this._displayIdMap.get(displayId) || [];
                        targets.push(model.length - 1);
                        //@ts-expect-error
                        this._displayIdMap.set(displayId, targets);
                    }
                    break;
                default:
                    //@ts-expect-error
                    this._onIOPub(msg);
                    break;
            }
            ;
        };
        this.cellId = cellId;
    }
    get future() {
        return super.future;
    }
    set future(value) {
        super.future = value;
        super.future.onIOPub = this.onIOPub;
    }
    createOutputItem(model) {
        const panel = super.createOutputItem(model);
        if (panel) {
            if (model.metadata['output_tag']) {
                const prompt = panel.widgets[0];
                prompt.outputTag = model.metadata['output_tag'];
            }
        }
        return panel;
    }
}
class DataflowOutputPrompt extends _jupyterlab_outputarea__WEBPACK_IMPORTED_MODULE_0__.OutputPrompt {
    constructor() {
        super(...arguments);
        this._outputTag = '';
    }
    updatePrompt() {
        if (this._outputTag) {
            this.node.textContent = `${this._outputTag}:`;
        }
        else if (this.executionCount === null) {
            this.node.textContent = '';
        }
        else {
            const cellId = this.executionCount.toString(16).padStart(8, '0');
            // .substr(0, 3);
            this.node.textContent = `[${cellId}]:`;
        }
    }
    get executionCount() {
        return super.executionCount;
    }
    set executionCount(value) {
        super.executionCount = value;
        this.updatePrompt();
    }
    get outputTag() {
        return this._outputTag;
    }
    set outputTag(value) {
        this._outputTag = value;
        this.updatePrompt();
    }
}
(function (DataflowOutputArea) {
    async function execute(code, output, sessionContext, metadata, dfData, cellIdModelMap) {
        var _a;
        // Override the default for `stop_on_error`.
        let stopOnError = true;
        if (metadata &&
            Array.isArray(metadata.tags) &&
            metadata.tags.indexOf('raises-exception') !== -1) {
            stopOnError = false;
        }
        if (dfData === undefined) {
            // FIXME not sure if this works or not...
            dfData = {};
        }
        const content = {
            code,
            stop_on_error: stopOnError,
            user_expressions: { __dfkernel_data__: dfData }
        };
        const kernel = (_a = sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel;
        if (!kernel) {
            throw new Error('Session has no kernel.');
        }
        const future = kernel.requestExecute(content, false, metadata);
        output.future = future;
        DataflowOutputArea.cellIdModelMap = cellIdModelMap;
        return future.done;
    }
    DataflowOutputArea.execute = execute;
    /**
     * The default implementation of `IContentFactory`.
     */
    class ContentFactory extends _jupyterlab_outputarea__WEBPACK_IMPORTED_MODULE_0__.OutputArea.ContentFactory {
        /**
         * Create the output prompt for the widget.
         */
        createOutputPrompt() {
            return new DataflowOutputPrompt();
        }
    }
    DataflowOutputArea.ContentFactory = ContentFactory;
    DataflowOutputArea.defaultContentFactory = new ContentFactory();
})(DataflowOutputArea || (DataflowOutputArea = {}));


/***/ })

}]);
//# sourceMappingURL=dfcells_lib_index_js.6aa2f25aca0588510138.js.map