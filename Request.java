package org.simplehttp;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashMap;

public final class Request
{
	
	public Response get(String url) throws MalformedURLException
	{
		return get(url, new HashMap<String, String>(), new HashMap<String, String>());
	}
	
	public Response get(String url, HashMap<String, String> parameters, String headers) throws MalformedURLException
	{
		return get(url, parameters, new HashMap<String, String>());
	}
	
	public Response get(String url, String parameters, HashMap<String, String> headers) throws MalformedURLException
	{
		return get(url, new HashMap<String, String>(), headers);
	}
	
	public Response get(String url, HashMap<String, String> parameters, HashMap<String, String> headers) throws MalformedURLException
	{
		URL requestUrl = null;
		Response response = new Response();
		try
		{
			if(parameters.size() > 0)
			{
				url = url.concat("?");
				boolean isFirstIter = true;
				for(String key : parameters.keySet())
				{
					if(!isFirstIter)
					{
						url = url.concat("&" + key + "=" + parameters.get(key));
					}
					else
					{
						url = url.concat(key + "=" + parameters.get(key));
						isFirstIter = false;
					}
				}
			}
			requestUrl = new URL(url);
			HttpURLConnection connection = (HttpURLConnection)requestUrl.openConnection();
			if(headers.size() != 0)
			{
				for(String header : headers.keySet())
				{
					connection.setRequestProperty(header, headers.get(header));
				}
			}
			connection.setRequestMethod("GET");
			response.responseText = "";
			response.statusCode = connection.getResponseCode(); 
			BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
			String responseLines;
			while((responseLines = reader.readLine()) != null)
			{
				response.responseText = response.responseText.concat(responseLines + "\n");
			}
			response.responseHeaders = connection.getHeaderFields();
			response.encoding = connection.getContentEncoding();
			connection.disconnect();
		} 
		catch(IOException e)
		{
			e.printStackTrace();
		}
		return response;
	}
	
	public Response post(String url) throws MalformedURLException
	{
		return post(url, new HashMap<String, String>(), new HashMap<String, String>());
	}
	
	public Response post(String url, HashMap<String, String> parameters, String headers) throws MalformedURLException
	{
		return post(url, parameters, new HashMap<String, String>());
	}
	
	public Response post(String url, String parameters, HashMap<String, String> headers) throws MalformedURLException
	{
		return post(url, new HashMap<String, String>(), headers);
	}
	
	public Response post(String url, HashMap<String, String> body, HashMap<String, String> headers) throws MalformedURLException
	{
		URL requestUrl = null;
		Response response = new Response();
		try
		{
			String requestBody = "";
			if(body.size() > 0)
			{
				url = url.concat("?");
				boolean isFirstIter = true;
				for(String key : body.keySet())
				{
					if(!isFirstIter)
					{
						requestBody = requestBody.concat("&" + key + "=" + body.get(key));
					}
					else
					{
						requestBody = requestBody.concat(key + "=" + body.get(key));
						isFirstIter = false;
					}
				}
			}
			requestUrl = new URL(url);
			HttpURLConnection connection = (HttpURLConnection)requestUrl.openConnection();
			if(headers.size() != 0)
			{
				for(String header : headers.keySet())
				{
					connection.setRequestProperty(header, headers.get(header));
				}
			}
			connection.setRequestMethod("POST");
			connection.setDoOutput(true);
			DataOutputStream dos = new DataOutputStream(connection.getOutputStream());
			dos.write(requestBody.getBytes("UTF-8"));
			response.responseText = "";
			response.statusCode = connection.getResponseCode(); 
			BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
			String responseLines;
			while((responseLines = reader.readLine()) != null)
			{
				response.responseText = response.responseText.concat(responseLines + "\n");
			}
			response.responseHeaders = connection.getHeaderFields();
			response.encoding = connection.getContentEncoding();
			connection.disconnect();
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		return response;
	}
}
