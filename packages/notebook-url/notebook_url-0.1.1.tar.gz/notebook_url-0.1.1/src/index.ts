import * as LZString from 'lz-string';
import { NotebookPanel, INotebookTracker } from '@jupyterlab/notebook';
import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { ToolbarButton } from '@jupyterlab/apputils';
import { Clipboard } from '@jupyterlab/apputils';

console.log('notebook_to_url_ext is loaded!');

// Compress the notebook text and set as URL parameter
function compressNotebookContent(notebookPanel: NotebookPanel): void {
    const notebookContent = JSON.stringify(notebookPanel.context.model.toJSON());
    const compressedContent = LZString.compressToEncodedURIComponent(notebookContent);
    const newUrl = `${window.location.origin}${window.location.pathname}#notebook=${compressedContent}`;
    Clipboard.copyToSystem(newUrl);
    alert('URL copied to clipboard');
}

// Decompress the URL parameter and load notebook content
function decompressNotebookContent(): any | null {
    const urlParams = new URLSearchParams(window.location.hash.slice(1));
    const compressedContent = urlParams.get('notebook');
    if (compressedContent) {
        const decompressedContent = LZString.decompressFromEncodedURIComponent(compressedContent);
        return JSON.parse(decompressedContent);
    }
    return null;
}

// Add "Save to URL" button to the notebook toolbar
function addSaveToUrlButton(app: JupyterFrontEnd, notebookTracker: INotebookTracker): void {
    const saveToUrlButton = new ToolbarButton({
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

const extension: JupyterFrontEndPlugin<void> = {
    id: 'notebook_to_url_ext',
    autoStart: true,
    requires: [INotebookTracker],
    activate: (app: JupyterFrontEnd, notebookTracker: INotebookTracker) => {
        console.log('Activating notebook_to_url_ext', app, notebookTracker);
        addSaveToUrlButton(app, notebookTracker);

        const initialContent = decompressNotebookContent();
        if (initialContent) {
            notebookTracker?.currentWidget?.context.model.fromJSON(initialContent);
        }
    }
};

// if (!window._JUPYTERLAB) {
//     window._JUPYTERLAB = {};
// }

// window._JUPYTERLAB['notebook_to_url_ext'] = extension;

export default extension;
