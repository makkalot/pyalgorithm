package com.makkalot.client;

import com.google.gwt.junit.client.GWTTestCase;

/**
 * GWT JUnit tests must extend GWTTestCase.
 */
public class StockObjectTest extends GWTTestCase {                       

  /**
   * Must refer to a valid module that sources this class.
   */
  public String getModuleName() {                                         
    return "com.makkalot.WithPlugin";
  }

  /**
   * Add as many tests as you like.
   */
  public void testSetters(){
	  StockObject s = new StockObject("xxx", 12.0, 0.2);
	   assertEquals(0.2, s.getChange());
	   assertEquals("xxx", s.getSymbol());
	   assertEquals(12.0, s.getPrice());
  }
  
  public void testStockParser(){
	  String xml_str = "<?xml version=\"1.0\" ?><stocks><stock><name>DD</name><price>59</price><change>0.1</change></stock></stocks>";
	  StockObject[] so = StockObject.parse_xml_stock(xml_str);
	  for(int i=0;i<so.length;i++){
		  assertEquals(0.1, so[i].getChange());
		  assertEquals("DD", so[i].getSymbol());
		  assertEquals(59.0, so[i].getPrice());
	  }
  }

}