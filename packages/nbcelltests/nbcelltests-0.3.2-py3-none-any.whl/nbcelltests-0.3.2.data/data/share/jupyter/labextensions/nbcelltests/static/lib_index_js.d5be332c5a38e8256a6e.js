"use strict";
(self["webpackChunknbcelltests"] = self["webpackChunknbcelltests"] || []).push([["lib_index_js"],{

/***/ "./lib/activate.js":
/*!*************************!*\
  !*** ./lib/activate.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   activate: () => (/* binding */ activate)
/* harmony export */ });
/* harmony import */ var _run__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./run */ "./lib/run.js");
/* harmony import */ var _tool__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./tool */ "./lib/tool.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./utils */ "./lib/utils.js");


// tslint:disable-next-line:max-line-length

function activate(app, docManager, palette, tracker, cellTools, editorServices) {
    /* Add to cell tools sidebar */
    const testsTool = new _tool__WEBPACK_IMPORTED_MODULE_0__.CelltestsTool(app, tracker, cellTools, editorServices);
    // Adds a section to notebookTools.
    cellTools.addSection({
        sectionName: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_ID,
        rank: 1,
        label: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_CATEGORY,
    });
    cellTools.addItem({ tool: testsTool, rank: 1.9, section: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_ID });
    /* Add to commands to sidebar */
    palette.addItem({ command: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_TEST_ID, category: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_CATEGORY });
    palette.addItem({ command: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_LINT_ID, category: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_CATEGORY });
    app.commands.addCommand(_utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_TEST_ID, {
        caption: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_TEST_CAPTION,
        execute: async () => {
            await (0,_run__WEBPACK_IMPORTED_MODULE_2__.runCellTests)(app, docManager);
        },
        isEnabled: (0,_utils__WEBPACK_IMPORTED_MODULE_1__.isEnabled)(app, docManager),
        label: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_TEST_CAPTION,
    });
    app.commands.addCommand(_utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_LINT_ID, {
        caption: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_LINT_CAPTION,
        execute: async () => {
            await (0,_run__WEBPACK_IMPORTED_MODULE_2__.runCellLints)(app, docManager);
        },
        isEnabled: (0,_utils__WEBPACK_IMPORTED_MODULE_1__.isEnabled)(app, docManager),
        label: _utils__WEBPACK_IMPORTED_MODULE_1__.CELLTESTS_LINT_CAPTION,
    });
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   _activate: () => (/* reexport safe */ _activate__WEBPACK_IMPORTED_MODULE_6__.activate),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/docmanager */ "webpack/sharing/consume/default/@jupyterlab/docmanager");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor");
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _style_index_css__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../style/index.css */ "./style/index.css");
/* harmony import */ var _activate__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./activate */ "./lib/activate.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./utils */ "./lib/utils.js");
/******************************************************************************
 *
 * Copyright (c) 2019, the nbcelltest authors.
 *
 * This file is part of the nbcelltest library, distributed under the terms of
 * the Apache License 2.0.  The full license can be found in the LICENSE file.
 *
 */








const extension = {
    activate: _activate__WEBPACK_IMPORTED_MODULE_6__.activate,
    autoStart: true,
    id: _utils__WEBPACK_IMPORTED_MODULE_7__.CELLTESTS_ID,
    optional: [_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_2__.ILauncher],
    requires: [_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1__.IDocumentManager, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__.INotebookTracker, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__.INotebookTools, _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_4__.IEditorServices],
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);



/***/ }),

/***/ "./lib/run.js":
/*!********************!*\
  !*** ./lib/run.js ***!
  \********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   runCellLints: () => (/* binding */ runCellLints),
/* harmony export */   runCellTests: () => (/* binding */ runCellTests)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__);
/******************************************************************************
 *
 * Copyright (c) 2019, the nbcelltest authors.
 *
 * This file is part of the nbcelltest library, distributed under the terms of
 * the Apache License 2.0.  The full license can be found in the LICENSE file.
 *
 */



async function runCellTests(app, docManager) {
    const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)({
        buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.cancelButton(), _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: "Ok" })],
        title: "Run tests?",
    });
    if (result.button.label === "Cancel") {
        return;
    }
    if (!app.shell.currentWidget) {
        return;
    }
    const context = docManager.contextForWidget(app.shell.currentWidget);
    if (context === undefined) {
        return;
    }
    const path = context.path;
    const model = context.model.toJSON();
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__.ServerConnection.makeSettings();
    const res = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__.ServerConnection.makeRequest(`${settings.baseUrl}celltests/test/run`, { method: "post", body: JSON.stringify({ path, model }) }, settings);
    if (res.ok) {
        const iframe = document.createElement("iframe");
        const html_data = (await res.json()).test;
        iframe.onload = () => {
            var _a;
            // write iframe content
            (_a = iframe.contentWindow) === null || _a === void 0 ? void 0 : _a.document.write(html_data);
        };
        const body = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget({ node: iframe });
        const dialog = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog({
            body,
            buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: "Ok" })],
            title: "Tests run!",
        });
        dialog.node.lastChild.style.maxHeight = "1600px";
        dialog.node.lastChild.style.maxWidth = "2000px";
        dialog.node.lastChild.style.width = "900px";
        dialog.node.lastChild.style.height = "900px";
        await dialog.launch();
    }
    else {
        await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)({
            body: "Check the Jupyter logs for the exception.",
            buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: "Ok" })],
            title: "Something went wrong!",
        });
    }
}
async function runCellLints(app, docManager) {
    const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)({
        buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.cancelButton(), _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: "Ok" })],
        title: "Run Lint?",
    });
    if (result.button.label === "Cancel") {
        return;
    }
    if (!app.shell.currentWidget) {
        return;
    }
    const context = docManager.contextForWidget(app.shell.currentWidget);
    if (context === undefined) {
        return;
    }
    const path = context.path;
    const model = context.model.toJSON();
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__.ServerConnection.makeSettings();
    const res = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__.ServerConnection.makeRequest(`${settings.baseUrl}celltests/lint/run`, { method: "post", body: JSON.stringify({ path, model }) }, settings);
    if (res.ok) {
        const div = document.createElement("div");
        div.innerHTML = (await res.json()).lint;
        const body = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget({ node: div });
        const dialog = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog({
            body,
            buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: "Ok" })],
            title: "Lints run!",
        });
        dialog.node.lastChild.style.maxHeight = "1600px";
        dialog.node.lastChild.style.maxWidth = "2000px";
        dialog.node.lastChild.style.width = "600px";
        dialog.node.lastChild.style.height = "800px";
        await dialog.launch();
    }
    else {
        await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)({
            body: "Check the Jupyter logs for the exception.",
            buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: "Ok" })],
            title: "Something went wrong!",
        });
    }
}


/***/ }),

/***/ "./lib/tool.js":
/*!*********************!*\
  !*** ./lib/tool.js ***!
  \*********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   CelltestsTool: () => (/* binding */ CelltestsTool)
/* harmony export */ });
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./utils */ "./lib/utils.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./widget */ "./lib/widget.js");
/******************************************************************************
 *
 * Copyright (c) 2019, the nbcelltest authors.
 *
 * This file is part of the nbcelltest library, distributed under the terms of
 * the Apache License 2.0.  The full license can be found in the LICENSE file.
 *
 */




class CelltestsTool extends _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.NotebookTools.Tool {
    constructor(app, notebook_Tracker, cellTools, editorServices) {
        super();
        this.notebookTracker = notebook_Tracker;
        this.cellTools = cellTools;
        this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.PanelLayout();
        /* Section Header */
        const label = document.createElement("label");
        label.textContent = "Celltests";
        this.layout.addWidget(new _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget({ node: label }));
        this.addClass(_utils__WEBPACK_IMPORTED_MODULE_2__.CELLTEST_TOOL_CLASS);
        this.widget = new _widget__WEBPACK_IMPORTED_MODULE_3__.CelltestsWidget(editorServices);
        this.widget.notebookTracker = notebook_Tracker;
        this.layout.addWidget(this.widget);
    }
    /**
     * Handle a change to the active cell.
     */
    onActiveCellChanged() {
        if (this.cellTools.activeCell) {
            this.widget.currentActiveCell = this.cellTools.activeCell;
            this.widget.loadTestsForActiveCell();
        }
    }
    // eslint-disable-next-line @typescript-eslint/no-empty-function
    onAfterShow() { }
    onAfterAttach() {
        var _a;
        if (this.notebookTracker.currentWidget === null) {
            return;
        }
        void this.notebookTracker.currentWidget.context.ready.then(() => {
            this.widget.loadTestsForActiveCell();
            this.widget.loadRulesForCurrentNotebook();
        });
        this.notebookTracker.currentChanged.connect(() => {
            this.widget.loadTestsForActiveCell();
            this.widget.loadRulesForCurrentNotebook();
        });
        (_a = this.notebookTracker.currentWidget.model) === null || _a === void 0 ? void 0 : _a.cells.changed.connect(() => {
            this.widget.loadTestsForActiveCell();
            this.widget.loadRulesForCurrentNotebook();
        });
    }
    onMetadataChanged(msg) {
        this.widget.loadTestsForActiveCell();
        this.widget.loadRulesForCurrentNotebook();
    }
}


/***/ }),

/***/ "./lib/utils.js":
/*!**********************!*\
  !*** ./lib/utils.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   CELLTESTS_CATEGORY: () => (/* binding */ CELLTESTS_CATEGORY),
/* harmony export */   CELLTESTS_ID: () => (/* binding */ CELLTESTS_ID),
/* harmony export */   CELLTESTS_LINT_CAPTION: () => (/* binding */ CELLTESTS_LINT_CAPTION),
/* harmony export */   CELLTESTS_LINT_ID: () => (/* binding */ CELLTESTS_LINT_ID),
/* harmony export */   CELLTESTS_TEST_CAPTION: () => (/* binding */ CELLTESTS_TEST_CAPTION),
/* harmony export */   CELLTESTS_TEST_ID: () => (/* binding */ CELLTESTS_TEST_ID),
/* harmony export */   CELLTEST_RULES: () => (/* binding */ CELLTEST_RULES),
/* harmony export */   CELLTEST_TOOL_CLASS: () => (/* binding */ CELLTEST_TOOL_CLASS),
/* harmony export */   CELLTEST_TOOL_CONTROLS_CLASS: () => (/* binding */ CELLTEST_TOOL_CONTROLS_CLASS),
/* harmony export */   CELLTEST_TOOL_EDITOR_CLASS: () => (/* binding */ CELLTEST_TOOL_EDITOR_CLASS),
/* harmony export */   CELLTEST_TOOL_RULES_CLASS: () => (/* binding */ CELLTEST_TOOL_RULES_CLASS),
/* harmony export */   isEnabled: () => (/* binding */ isEnabled)
/* harmony export */ });
/******************************************************************************
 *
 * Copyright (c) 2019, the nbcelltest authors.
 *
 * This file is part of the nbcelltest library, distributed under the terms of
 * the Apache License 2.0.  The full license can be found in the LICENSE file.
 *
 */
const CELLTESTS_ID = "nbcelltests";
const CELLTESTS_CATEGORY = "Cell Tests";
const CELLTESTS_TEST_ID = "nbcelltests:test";
const CELLTESTS_LINT_ID = "nbcelltests:lint";
const CELLTESTS_TEST_CAPTION = "Run Celltests";
const CELLTESTS_LINT_CAPTION = "Run Lint";
const CELLTEST_TOOL_CLASS = "CelltestTool";
const CELLTEST_TOOL_CONTROLS_CLASS = "CelltestsControls";
const CELLTEST_TOOL_RULES_CLASS = "CelltestsRules";
const CELLTEST_TOOL_EDITOR_CLASS = "CelltestsEditor";
const CELLTEST_RULES = [
    // TODO fetch from server
    {
        key: "lines_per_cell",
        label: "Lines per Cell",
        min: 1,
        step: 1,
        value: 10,
    },
    {
        key: "cells_per_notebook",
        label: "Cells per Notebook",
        min: 1,
        step: 1,
        value: 20,
    },
    {
        key: "function_definitions",
        label: "Function definitions",
        min: 0,
        step: 1,
        value: 10,
    },
    {
        key: "class_definitions",
        label: "Class definitions",
        min: 0,
        step: 1,
        value: 5,
    },
    {
        key: "cell_coverage",
        label: "Cell test coverage (%)",
        max: 100,
        min: 1,
        step: 1,
        value: 50,
    },
];
function isEnabled(app, docManager) {
    return () => { var _a; return !!(app.shell.currentWidget && docManager.contextForWidget(app.shell.currentWidget) && ((_a = docManager.contextForWidget(app.shell.currentWidget)) === null || _a === void 0 ? void 0 : _a.model)); };
}


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   CelltestsWidget: () => (/* binding */ CelltestsWidget)
/* harmony export */ });
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/cells */ "webpack/sharing/consume/default/@jupyterlab/cells");
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_cells__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor");
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _style_circle_svg__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../style/circle.svg */ "./style/circle.svg");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./utils */ "./lib/utils.js");
/******************************************************************************
 *
 * Copyright (c) 2019, the nbcelltest authors.
 *
 * This file is part of the nbcelltest library, distributed under the terms of
 * the Apache License 2.0.  The full license can be found in the LICENSE file.
 *
 */
/* eslint-disable max-classes-per-file */
/* eslint-disable id-blacklist */





const DEFAULT_TESTS = ['# Use %cell to mark where the cell should be inserted, or add a line comment "# no %cell" to deliberately skip the cell\n', "%cell\n"];
/**
 * Widget responsible for holding test controls
 *
 * @class      ControlsWidget (name)
 */
class ControlsWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.BoxPanel {
    constructor() {
        super({ direction: "top-to-bottom" });
        // eslint-disable-next-line @typescript-eslint/no-empty-function
        this.add = () => { };
        // eslint-disable-next-line @typescript-eslint/no-empty-function
        this.save = () => { };
        // eslint-disable-next-line @typescript-eslint/no-empty-function
        this.clear = () => { };
        /* Section Header */
        this.label = document.createElement("label");
        this.label.textContent = "Tests";
        this.svglabel = document.createElement("label");
        this.svg = document.createElement("svg");
        this.svg.innerHTML = _style_circle_svg__WEBPACK_IMPORTED_MODULE_3__;
        this.svg = this.svg.firstChild;
        const div1 = document.createElement("div");
        div1.appendChild(this.label);
        const div2 = document.createElement("div");
        div1.appendChild(div2);
        div2.appendChild(this.svglabel);
        div2.appendChild(this.svg);
        this.node.appendChild(div1);
        this.node.classList.add(_utils__WEBPACK_IMPORTED_MODULE_4__.CELLTEST_TOOL_CONTROLS_CLASS);
        /* Add button */
        const div3 = document.createElement("div");
        const add = document.createElement("button");
        add.textContent = "Add";
        add.onclick = () => {
            this.add();
        };
        /* Save button */
        const save = document.createElement("button");
        save.textContent = "Save";
        save.onclick = () => {
            this.save();
        };
        /* Clear button */
        const clear = document.createElement("button");
        clear.textContent = "Clear";
        clear.onclick = () => {
            this.clear();
        };
        /* add to container */
        div3.appendChild(add);
        div3.appendChild(save);
        div3.appendChild(clear);
        this.node.appendChild(div3);
    }
}
/**
 * Widget responsible for holding test controls
 *
 * @class      ControlsWidget (name)
 */
class RulesWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.BoxPanel {
    constructor() {
        super({ direction: "top-to-bottom" });
        // eslint-disable-next-line @typescript-eslint/no-empty-function
        this.save = () => { };
        /* Section Header */
        this.label = document.createElement("label");
        this.label.textContent = "Lint Rules";
        this.node.appendChild(this.label);
        this.node.classList.add(_utils__WEBPACK_IMPORTED_MODULE_4__.CELLTEST_TOOL_RULES_CLASS);
        /* Add button */
        const div = document.createElement("div");
        [].slice.call(_utils__WEBPACK_IMPORTED_MODULE_4__.CELLTEST_RULES).forEach((val) => {
            const row = document.createElement("div");
            const span = document.createElement("span");
            span.textContent = val.label;
            const chkbx = document.createElement("input");
            chkbx.type = "checkbox";
            chkbx.name = val.key;
            const number = document.createElement("input");
            number.type = "number";
            number.name = val.key;
            chkbx.onchange = () => {
                number.disabled = !chkbx.checked;
                number.value = number.disabled ? "" : val.value;
                this.save();
            };
            number.onchange = () => {
                this.save();
            };
            if (val.min !== undefined) {
                number.min = val.min;
            }
            if (val.max !== undefined) {
                number.max = val.max;
            }
            if (val.step !== undefined) {
                number.step = val.step;
            }
            row.appendChild(span);
            row.appendChild(chkbx);
            row.appendChild(number);
            this.setByKey(val.key, row);
            div.appendChild(row);
        });
        this.node.appendChild(div);
    }
    getByKey(key) {
        switch (key) {
            case "lines_per_cell": {
                return this.lines_per_cell;
            }
            case "cells_per_notebook": {
                return this.cells_per_notebook;
            }
            case "function_definitions": {
                return this.function_definitions;
            }
            case "class_definitions": {
                return this.class_definitions;
            }
            case "cell_coverage": {
                return this.cell_coverage;
            }
            default:
                return undefined;
        }
    }
    setByKey(key, elem) {
        switch (key) {
            case "lines_per_cell": {
                this.lines_per_cell = elem;
                break;
            }
            case "cells_per_notebook": {
                this.cells_per_notebook = elem;
                break;
            }
            case "function_definitions": {
                this.function_definitions = elem;
                break;
            }
            case "class_definitions": {
                this.class_definitions = elem;
                break;
            }
            case "cell_coverage": {
                this.cell_coverage = elem;
                break;
            }
            default:
        }
    }
    getValuesByKey(key) {
        let elem;
        switch (key) {
            case "lines_per_cell": {
                elem = this.lines_per_cell;
                break;
            }
            case "cells_per_notebook": {
                elem = this.cells_per_notebook;
                break;
            }
            case "function_definitions": {
                elem = this.function_definitions;
                break;
            }
            case "class_definitions": {
                elem = this.class_definitions;
                break;
            }
            case "cell_coverage": {
                elem = this.cell_coverage;
                break;
            }
            default:
                return { key, enabled: false, value: 0 };
        }
        const chkbx = elem.querySelector('input[type="checkbox"]');
        const input = elem.querySelector('input[type="number"]');
        return { key, enabled: chkbx.checked, value: Number(input.value) };
    }
    setValuesByKey(key, checked = true, value = null) {
        let elem;
        switch (key) {
            case "lines_per_cell": {
                elem = this.lines_per_cell;
                break;
            }
            case "cells_per_notebook": {
                elem = this.cells_per_notebook;
                break;
            }
            case "function_definitions": {
                elem = this.function_definitions;
                break;
            }
            case "class_definitions": {
                elem = this.class_definitions;
                break;
            }
            case "cell_coverage": {
                elem = this.cell_coverage;
                break;
            }
            default:
                return;
        }
        const chkbx = elem.querySelector('input[type="checkbox"]');
        const input = elem.querySelector('input[type="number"]');
        if (input) {
            input.value = value === null ? "" : String(value);
            input.disabled = !checked;
        }
        if (chkbx) {
            chkbx.checked = checked;
        }
    }
}
/**
 * Widget holding the Celltests widget, container for options and editor
 *
 * @class      CelltestsWidget (name)
 */
class CelltestsWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    constructor(editorServices) {
        super();
        /* create layout */
        this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.PanelLayout();
        /* create options widget */
        this.controls = new ControlsWidget();
        /* create options widget */
        this.rules = new RulesWidget();
        /* create codemirror editor */
        const editorOptions = {
            factory: editorServices.factoryService.newInlineEditor,
            model: new _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_1__.CodeCellModel({}),
        };
        this.editor = new _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.CodeEditorWrapper(editorOptions);
        this.editor.addClass(_utils__WEBPACK_IMPORTED_MODULE_4__.CELLTEST_TOOL_EDITOR_CLASS);
        this.editor.model.mimeType = "text/x-ipython";
        /* add options and editor to widget */
        this.layout.addWidget(this.controls);
        this.layout.addWidget(this.editor);
        this.layout.addWidget(this.rules);
        /* set add button functionality */
        this.controls.add = () => {
            this.fetchAndSetTests();
            return true;
        };
        /* set save button functionality */
        this.controls.save = () => {
            this.saveTestsForActiveCell();
            return true;
        };
        /* set clear button functionality */
        this.controls.clear = () => {
            this.deleteTestsForActiveCell();
            return true;
        };
        this.rules.save = () => {
            this.saveRulesForCurrentNotebook();
        };
        this.fetchAndSetTests.bind(this);
        this.loadTestsForActiveCell.bind(this);
        this.saveTestsForActiveCell.bind(this);
        this.deleteTestsForActiveCell.bind(this);
        this.loadRulesForCurrentNotebook.bind(this);
        this.setIndicatorNoTests.bind(this);
        this.setIndicatorTests.bind(this);
        this.setIndicatorNonCode.bind(this);
    }
    fetchAndSetTests() {
        const tests = [];
        const splits = this.editor.model.sharedModel.source.split(/\n/);
        splits.forEach(split => {
            tests.push(`${split}\n`);
        });
        if (this.currentActiveCell !== null && this.currentActiveCell.model.type === "code") {
            this.currentActiveCell.model.setMetadata("celltests", tests);
            this.setIndicatorTests();
        }
    }
    loadTestsForActiveCell() {
        if (this.currentActiveCell !== null && this.currentActiveCell.model.type === "code") {
            let tests = this.currentActiveCell.model.getMetadata("tests");
            if (tests === undefined || tests.length === 0) {
                tests = DEFAULT_TESTS;
                this.setIndicatorNoTests();
            }
            else {
                this.setIndicatorTests();
            }
            this.editor.model.sharedModel.source = tests.join("");
            this.editor.editor.setOption("readOnly", false);
        }
        else {
            this.editor.model.sharedModel.source = "# Not a code cell";
            this.editor.editor.setOption("readOnly", true);
            this.setIndicatorNonCode();
        }
    }
    saveTestsForActiveCell() {
        /* if currentActiveCell exists */
        if (this.currentActiveCell !== null && this.currentActiveCell.model.type === "code") {
            const tests = [];
            const splits = this.editor.model.sharedModel.getSource().split(/\n/);
            splits.forEach(split => {
                tests.push(`${split}\n`);
            });
            this.currentActiveCell.model.setMetadata("tests", tests);
            this.setIndicatorTests();
        }
        else if (this.currentActiveCell !== null) {
            // TODO this?
            this.currentActiveCell.model.deleteMetadata("tests");
            this.setIndicatorNonCode();
        }
    }
    deleteTestsForActiveCell() {
        if (this.currentActiveCell !== null) {
            this.editor.model.sharedModel.source = "";
            this.currentActiveCell.model.deleteMetadata("tests");
            this.setIndicatorNoTests();
        }
    }
    loadRulesForCurrentNotebook() {
        var _a, _b;
        if (this.notebookTracker !== null) {
            const metadata = ((_b = (_a = this.notebookTracker.currentWidget) === null || _a === void 0 ? void 0 : _a.model) === null || _b === void 0 ? void 0 : _b.getMetadata("celltests")) || {};
            [].slice.call(_utils__WEBPACK_IMPORTED_MODULE_4__.CELLTEST_RULES).forEach((rule) => {
                this.rules.setValuesByKey(rule.key, rule.key in metadata, metadata[rule.key]);
            });
        }
    }
    saveRulesForCurrentNotebook() {
        var _a, _b;
        if (this.notebookTracker !== null) {
            const metadata = {};
            [].slice.call(_utils__WEBPACK_IMPORTED_MODULE_4__.CELLTEST_RULES).forEach((rule) => {
                const settings = this.rules.getValuesByKey(rule.key);
                if (settings.enabled) {
                    metadata[settings.key] = settings.value;
                }
            });
            (_b = (_a = this.notebookTracker.currentWidget) === null || _a === void 0 ? void 0 : _a.model) === null || _b === void 0 ? void 0 : _b.setMetadata("celltests", metadata);
        }
    }
    get editorWidget() {
        return this.editor;
    }
    setIndicatorNoTests() {
        var _a;
        ((_a = this.controls.svg.firstElementChild) === null || _a === void 0 ? void 0 : _a.firstElementChild).style.fill = "#e75c57";
        this.controls.svglabel.textContent = "(No Tests)";
    }
    setIndicatorTests() {
        var _a;
        ((_a = this.controls.svg.firstElementChild) === null || _a === void 0 ? void 0 : _a.firstElementChild).style.fill = "#008000";
        this.controls.svglabel.textContent = "(Tests Exist)";
    }
    setIndicatorNonCode() {
        var _a;
        ((_a = this.controls.svg.firstElementChild) === null || _a === void 0 ? void 0 : _a.firstElementChild).style.fill = "var(--jp-inverse-layout-color3)";
        this.controls.svglabel.textContent = "(Non Code Cell)";
    }
}


/***/ }),

/***/ "./style/circle.svg":
/*!**************************!*\
  !*** ./style/circle.svg ***!
  \**************************/
/***/ ((module) => {

module.exports = "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 18 18\" width=\"16\" data-icon=\"ui-components:circle\" data-icon-id=\"7d9ec9fd-2068-44cd-9487-e1b99034e445\">\n    <g class=\"jp-icon3\" fill=\"#616161\">\n        <circle cx=\"9\" cy=\"9\" r=\"8\"></circle>\n    </g>\n</svg>";

/***/ })

}]);
//# sourceMappingURL=lib_index_js.d5be332c5a38e8256a6e.js.map