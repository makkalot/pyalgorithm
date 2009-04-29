package com.makkalot.client;

import java.util.ArrayList;
import java.util.Iterator;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.event.dom.client.ClickEvent;
import com.google.gwt.event.dom.client.ClickHandler;
import com.google.gwt.event.dom.client.KeyCodes;
import com.google.gwt.event.dom.client.KeyPressEvent;
import com.google.gwt.event.dom.client.KeyPressHandler;
import com.google.gwt.http.client.URL;
import com.google.gwt.i18n.client.NumberFormat;
import com.google.gwt.user.client.Timer;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.VerticalPanel;

import com.google.gwt.http.client.Request;
import com.google.gwt.http.client.RequestBuilder;
import com.google.gwt.http.client.RequestCallback;
import com.google.gwt.http.client.RequestException;
import com.google.gwt.http.client.Response;


/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class WithPlugin implements EntryPoint {

	private static final int REFRESH_INTERVAL = 5000;
	private VerticalPanel mainPanel = new VerticalPanel();
	  private FlexTable stocksFlexTable = new FlexTable();
	  private HorizontalPanel addPanel = new HorizontalPanel();
	  private TextBox newSymbolTextBox = new TextBox();
	  private Button addStockButton = new Button("Add");
	  //private Label lastUpdatedLabel = new Label();
	  private ArrayList<String> stocks = new ArrayList<String>();

	  
	@Override
	public void onModuleLoad() {
		// TODO Auto-generated method stub
		stocksFlexTable.setText(0, 0, "Symbol");
	    stocksFlexTable.setText(0, 1, "Price");
	    stocksFlexTable.setText(0, 2, "Change");
	    stocksFlexTable.setText(0, 3, "Remove");

	    addPanel.add(newSymbolTextBox);
	    addPanel.add(addStockButton);
	    
	    mainPanel.add(stocksFlexTable);
	    mainPanel.add(addPanel);
	    //mainPanel.add(lastUpdatedLabel);
	    
	    RootPanel.get("stockList").add(mainPanel);
	    
	    newSymbolTextBox.setFocus(true);
	    
	    //add the handlers
	    addStockButton.addClickHandler(new ClickHandler() {
	        
	    	@Override
			public void onClick(ClickEvent event) {
				// TODO Auto-generated method stub
				addStock();
			}

			
	      });

	 // Listen for keyboard events in the input box.
	    newSymbolTextBox.addKeyPressHandler(new KeyPressHandler() {
	      public void onKeyPress(KeyPressEvent event) {
	        if (event.getCharCode() == KeyCodes.KEY_ENTER) {
	          addStock();
	        }
	      }
	    });
	    
	    Timer refreshTimer = new Timer() {
	        @Override
	        public void run() {
	          refreshWatchList();
	        }
	      };
	      refreshTimer.scheduleRepeating(REFRESH_INTERVAL);




	}
  protected void refreshWatchList() {
		// TODO Auto-generated method stub
	  String url = "/stocker/?q=";

	  //that on is wrong also have to fix it
	  Iterator iter = stocks.iterator();
	    while (iter.hasNext()) {
	      url += iter.next();
	      if (iter.hasNext()) {
	        url += "+";
	      }
	    }

	    url = URL.encode(url);

	    //updateTable(prices);
	    RequestBuilder builder = new RequestBuilder(RequestBuilder.GET, url);
	    try {
	        Request request = builder.sendRequest(null, new RequestCallback() {
	          public void onError(Request request, Throwable exception) {
	            displayError("Couldn't retrieve XML data");
	          }

	          public void onResponseReceived(Request request, Response response) {
	            if (200 == response.getStatusCode()) {
	              //Window.alert("What we got is "+response.getText());
	            	StockObject[] so =StockObject.parse_xml_stock(response.getText());
	              
	              updateTable(so);
	            } else {
	              displayError("Couldn't retrieve XMLL data (" + response.getStatusText()
	                  + ")");
	            }
	          }
	        });
	      } catch (RequestException e) {
	        displayError("Couldn't retrieve sorry "+e.toString());
	      }
	      catch (Exception e) {
			// TODO: handle exception
	    	  displayError("Wow big error "+e.toString());
		}
		
	}
private void displayError(String string) {
	// TODO Auto-generated method stub
	Window.alert("We have error "+string);
	
}
private void updateTable(StockObject[] prices) {
	// TODO Auto-generated method stub
	for (int i = 0; i < prices.length; i++) {
	      updateTable(prices[i]);
	    }

	
}
private void updateTable(StockObject price) {
	// TODO Auto-generated method stub
	if (!stocks.contains(price.getSymbol())) {
	      return;
	    }

	    int row = stocks.indexOf(price.getSymbol()) + 1;

	    // Format the data in the Price and Change fields.
	    String priceText = NumberFormat.getFormat("#,##0.00").format(
	        price.getPrice());
	    NumberFormat changeFormat = NumberFormat.getFormat("+#,##0.00;-#,##0.00");
	    String changeText = changeFormat.format(price.getChange());
	    String changePercentText = changeFormat.format(price.getChangePercent());

	    // Populate the Price and Change fields with new data.
	    stocksFlexTable.setText(row, 1, priceText);
	    stocksFlexTable.setText(row, 2, changeText + " (" + changePercentText
	        + "%)");

	
}
/**
   * The message displayed to the user when the server cannot be reached or
   * returns an error.
   */
	
	private void addStock() {
		// TODO Auto-generated method stub
		final String symbol = newSymbolTextBox.getText().toUpperCase().trim();
	    newSymbolTextBox.setFocus(true);

	    // Stock code must be between 1 and 10 chars that are numbers, letters, or dots.
	    if (!symbol.matches("^[0-9a-zA-Z\\.]{1,10}$")) {
	      Window.alert("'" + symbol + "' is not a valid symbol.");
	      newSymbolTextBox.selectAll();
	      return;
	    }

	    newSymbolTextBox.setText("");
	    
	    if (stocks.contains(symbol))
	        return;

	    int row = stocksFlexTable.getRowCount();
	    stocks.add(symbol);
	    stocksFlexTable.setText(row, 0, symbol);
	    
	    Button removeStockButton = new Button("x");
	    removeStockButton.addClickHandler(new ClickHandler() {
	      public void onClick(ClickEvent event) {
	        int removedIndex = stocks.indexOf(symbol);
	        stocks.remove(removedIndex);
	        stocksFlexTable.removeRow(removedIndex + 1);
	      }
	    });
	    stocksFlexTable.setWidget(row, 3, removeStockButton);
		
	    refreshWatchList();
	}
  
}
