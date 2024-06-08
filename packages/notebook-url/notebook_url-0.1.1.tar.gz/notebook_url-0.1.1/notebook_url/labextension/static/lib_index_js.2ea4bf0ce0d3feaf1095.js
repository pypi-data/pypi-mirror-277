"use strict";
(self["webpackChunknotebook_url"] = self["webpackChunknotebook_url"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var lz_string__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! lz-string */ "webpack/sharing/consume/default/lz-string/lz-string");
/* harmony import */ var lz_string__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(lz_string__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);




console.log('notebook_to_url_ext is loaded!');
// Compress the notebook text and set as URL parameter
function compressNotebookContent(notebookPanel) {
    const notebookContent = JSON.stringify(notebookPanel.context.model.toJSON());
    const compressedContent = lz_string__WEBPACK_IMPORTED_MODULE_0__.compressToEncodedURIComponent(notebookContent);
    const newUrl = `${window.location.origin}${window.location.pathname}#notebook=${compressedContent}`;
    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.Clipboard.copyToSystem(newUrl);
    alert('URL copied to clipboard');
}
// Decompress the URL parameter and load notebook content
function decompressNotebookContent() {
    const urlParams = new URLSearchParams(window.location.hash.slice(1));
    const compressedContent = urlParams.get('notebook');
    if (compressedContent) {
        const decompressedContent = lz_string__WEBPACK_IMPORTED_MODULE_0__.decompressFromEncodedURIComponent(compressedContent);
        return JSON.parse(decompressedContent);
    }
    return null;
}
// Add "Save to URL" button to the notebook toolbar
function addSaveToUrlButton(app, notebookTracker) {
    const saveToUrlButton = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.ToolbarButton({
        label: 'Save to URL',
        onClick: () => {
            const current = notebookTracker.currentWidget;
            if (current) {
                compressNotebookContent(current);
            }
        },
        tooltip: 'Save notebook content to URL and copy to clipboard'
    });
    notebookTracker.widgetAdded.connect((sender, panel) => {
        panel.toolbar.insertItem(10, 'saveToUrl', saveToUrlButton);
    });
}
const extension = {
    id: 'notebook_to_url_ext',
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.INotebookTracker],
    activate: (app, notebookTracker) => {
        var _a;
        console.log('Activating notebook_to_url_ext', app, notebookTracker);
        addSaveToUrlButton(app, notebookTracker);
        const initialContent = decompressNotebookContent();
        if (initialContent) {
            (_a = notebookTracker === null || notebookTracker === void 0 ? void 0 : notebookTracker.currentWidget) === null || _a === void 0 ? void 0 : _a.context.model.fromJSON(initialContent);
        }
    }
};
// if (!window._JUPYTERLAB) {
//     window._JUPYTERLAB = {};
// }
// window._JUPYTERLAB['notebook_to_url_ext'] = extension;
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.2ea4bf0ce0d3feaf1095.js.map