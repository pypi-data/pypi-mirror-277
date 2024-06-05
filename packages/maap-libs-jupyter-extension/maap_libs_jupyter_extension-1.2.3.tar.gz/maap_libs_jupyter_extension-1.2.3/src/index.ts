import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { IDisposable, DisposableDelegate } from '@lumino/disposable';
import { ToolbarButton } from '@jupyterlab/apputils';
import { DocumentRegistry } from '@jupyterlab/docregistry';
import { NotebookActions, NotebookPanel, INotebookModel } from '@jupyterlab/notebook';
import { ElementExt } from '@lumino/domutils';
import { Notification } from "@jupyterlab/apputils";
import { PageConfig } from '@jupyterlab/coreutils'
import { request, RequestResult } from './request';
import '../style/index.css';

let DEFAULT_CODE = 'from maap.maap import MAAP\n' +
                     'maap = MAAP()';

let api_server = '';
var valuesUrl = new URL(PageConfig.getBaseUrl() + 'jupyter-server-extension/getConfig');

request('get', valuesUrl.href).then((res: RequestResult) => {
  if (res.ok) {
    let environment = JSON.parse(res.data);
    api_server = environment['api_server'];
    DEFAULT_CODE = 'from maap.maap import MAAP\n' +
                     'maap = MAAP(maap_host=\'' + api_server + '\')';
  }
}); 

/**
 * A notebook widget extension that adds a button to the toolbar.
 */
export class ButtonExtension implements DocumentRegistry.IWidgetExtension<NotebookPanel, INotebookModel> {
    /**
     * Create a new extension object.
     */
    createNew(panel: NotebookPanel, context: DocumentRegistry.IContext<INotebookModel>): IDisposable {
        let callback = () => {

            // Select the first cell of the notebook
            panel.content.activeCellIndex = 0;
            panel.content.deselectAll();
            if (panel.content.activeCell != null) {
              ElementExt.scrollIntoViewIfNeeded(
                  panel.content.node,
                  panel.content.activeCell.node
              );
            }

          // Check if already there
          if (panel.content.activeCell != null) {
            if (panel.content.activeCell.model.sharedModel.getSource() == DEFAULT_CODE) {
              Notification.error("MAAP defaults already imported to notebook.");
            }
            else {
              // Insert code above selected first cell
              NotebookActions.insertAbove(panel.content);
              panel.content.activeCell.model.sharedModel.setSource(DEFAULT_CODE);
            }
          }

        };

        let button = new ToolbarButton({
            className: 'myButton',
            iconClass: 'jp-MaapIcon foo jp-Icon jp-Icon-16 jp-ToolbarButtonComponent-icon',
            onClick: callback,
            tooltip: 'Import MAAP Libraries'
        });

        panel.toolbar.insertItem(0,'insertDefaults', button);
        return new DisposableDelegate(() => {
            button.dispose();
        });
    }
}

/**
 * Activate the extension.
 */
function activateNbDefaults(app: JupyterFrontEnd) {
    app.docRegistry.addWidgetExtension('Notebook', new ButtonExtension());
    console.log("JupyterLab MAAP Libraries extension activated!");
};

/**
 * Initialization data for the insert_defaults_to_notebook extension.
 */
const extensionNbDefaults: JupyterFrontEndPlugin<void> = {
    id: 'insert_defaults_to_notebook',
    autoStart: true,
    activate: activateNbDefaults
};

export default [extensionNbDefaults];