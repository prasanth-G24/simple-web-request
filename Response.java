package org.simplehttp;

import java.util.List;
import java.util.Map;
import org.json.JSONObject;

public final class Response 
{
	public int statusCode;
	public String responseText;
	public String encoding;
	public Map<String, List<String>> responseHeaders;
	
	public List<String> getHeader(String header)
	{
		return responseHeaders.get(header);
	}
	
	public JSONObject getJSONResponse()
	{
		return new JSONObject(responseText);
	}
}
