package com.makkalot.client;

import com.google.gwt.user.client.Window;
import com.google.gwt.xml.client.DOMException;
import com.google.gwt.xml.client.Document;
import com.google.gwt.xml.client.Node;
import com.google.gwt.xml.client.NodeList;
import com.google.gwt.xml.client.XMLParser;

public class StockObject {
	private String symbol;
	  private double price;
	  private double change;
	
	  
	  public StockObject(String symbol, double price, double change) {
		super();
		this.symbol = symbol;
		this.price = price;
		this.change = change;
	}

	  public StockObject() {
			super();
			}
	  
	public String getSymbol() {
		return symbol;
	}


	public void setSymbol(String symbol) {
		this.symbol = symbol;
	}


	public double getPrice() {
		return price;
	}

	public double getChangePercent() {
	    return 10.0 * this.change / this.price;
	  }

	public void setPrice(double price) {
		this.price = price;
	}


	public double getChange() {
		return change;
	}


	public void setChange(double change) {
		this.change = change;
	}
	  
	public static StockObject[] parse_xml_stock(String xml_str){
		try {
		    // parse the XML document into a DOM
		    Document messageDom =  XMLParser.parse(xml_str);
		    
		    // find the sender's display name in an attribute of the <from> tag
		    Node stocks_node = messageDom.getElementsByTagName("stocks").item(0);
		    //System.out.println("The main node name is "+stocks_node.getNodeName());
		    NodeList list_stocks = stocks_node.getChildNodes();
		    
		    //create the array
		    int array_length = list_stocks.getLength();
		    //System.out.println("The main nodes children are "+array_length);
		    StockObject[] so=new StockObject[array_length];
		    
		    for(int i=0;i<array_length;i++){
		    	//we reached now to "stock" part we have to get now its children
		    	NodeList nl_tmp= list_stocks.item(i).getChildNodes();
		    	//System.out.println("The nodes of stocks are  "+nl_tmp.getLength());
		    	//alocate the space for it 
		    	so[i]=new StockObject();
		    	
		    	int stocks_length = nl_tmp.getLength();
		    	for (int j=0;j<stocks_length;j++){
		    		//now u can extract em lol
		    		//System.out.println("BEFORE The tmp node is ");
		    		String tmp_node_name = nl_tmp.item(j).getNodeName();
		    		//System.out.println("The tmp node is "+tmp_node_name);
		    		if(tmp_node_name.equals("price")){
		    			//System.out.println("The price is " +Double.parseDouble(nl_tmp.item(j).getNodeValue()));
		    			so[i].setPrice(Double.parseDouble((String)nl_tmp.item(j).getFirstChild().getNodeValue()));
		    			
		    		}
		    		else
		    			if(tmp_node_name.equals("change")){
		    				//System.out.println("The change is " +Double.parseDouble(nl_tmp.item(j).getFirstChild().getNodeValue()));
		    				so[i].setChange(Double.parseDouble((String)nl_tmp.item(j).getFirstChild().getNodeValue()));
		    				
		    			}
		    			else
		    				if(tmp_node_name.equals("name")){
		    					//sSystem.out.println("The name is " +(String)nl_tmp.item(j).getFirstChild().getNodeValue());
		    					so[i].setSymbol((String)nl_tmp.item(j).getFirstChild().getNodeValue());
		    					}
		    		//System.out.println("END of the for is here ? ");	
		    	}
		    	
		    }
		    
		    return so;
		  } catch (DOMException e) {
		    Window.alert("Could not parse XML document.");
		    //System.out.println("Could not parse XML document." + e.toString());
		  }
		  return null;

	}   

	  
}
