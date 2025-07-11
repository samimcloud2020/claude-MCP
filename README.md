# claude-MCP
                                                                                                                                                                                                                           
PS C:\WINDOWS\system32> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"             
Downloading uv 0.7.20 (x86_64-pc-windows-msvc)                                                                          
Installing to C:\Users\Lenovo\.local\bin
  uv.exe
  uvx.exe
  uvw.exe
everything's installed!

To add C:\Users\Lenovo\.local\bin to your PATH, either restart your shell or run:

    set Path=C:\Users\Lenovo\.local\bin;%Path%   (cmd)
    $env:Path = "C:\Users\Lenovo\.local\bin;$env:Path"   (powershell)

    
PS C:\WINDOWS\system32> $env:Path = "C:\Users\Lenovo\.local\bin;$env:Path"

PS C:\WINDOWS\system32> uv init StockAnalysisServer
Initialized project `stockanalysisserver` at `C:\WINDOWS\system32\StockAnalysisServer`

PS C:\WINDOWS\system32> cd  StockAnalysisServer

PS C:\WINDOWS\system32\StockAnalysisServer> uv venv
Using CPython 3.13.5 interpreter at: C:\Users\Lenovo\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate

PS C:\WINDOWS\system32\StockAnalysisServer> .venv\Scripts\activate
(StockAnalysisServer) PS C:\WINDOWS\system32\StockAnalysisServer> uv add mcp[cli] httpx
Resolved 35 packages in 14.03s
Prepared 34 packages in 1m 06s
Installed 34 packages in 20.66s
 + annotated-types==0.7.0
 + anyio==4.9.0
 + attrs==25.3.0
 + certifi==2025.7.9
 + click==8.2.1
 + colorama==0.4.6
 + h11==0.16.0
 + httpcore==1.0.9
 + httpx==0.28.1
 + httpx-sse==0.4.1
 + idna==3.10
 + jsonschema==4.24.0
 + jsonschema-specifications==2025.4.1
 + markdown-it-py==3.0.0
 + mcp==1.11.0
 + mdurl==0.1.2
 + pydantic==2.11.7
 + pydantic-core==2.33.2
 + pydantic-settings==2.10.1
 + pygments==2.19.2
 + python-dotenv==1.1.1
 + python-multipart==0.0.20
 + pywin32==310
 + referencing==0.36.2
 + rich==14.0.0
 + rpds-py==0.26.0
 + shellingham==1.5.4
 + sniffio==1.3.1
 + sse-starlette==2.4.1
 + starlette==0.47.1
 + typer==0.16.0
 + typing-extensions==4.14.1
 + typing-inspection==0.4.1
 + uvicorn==0.35.0
 + 
(StockAnalysisServer) PS C:\WINDOWS\system32\StockAnalysisServer> uv add fastmcp yfinance python-dotenv pandas numpy uvicorn fastapi
Resolved 69 packages in 45.72s
      Built peewee==3.18.2
      Built pyperclip==1.9.0
Prepared 35 packages in 2m 13s
Uninstalled 1 package in 3.25s
Installed 35 packages in 15.10s
 + authlib==1.6.0
 + beautifulsoup4==4.13.4
 + cffi==1.17.1
 + charset-normalizer==3.4.2
 + cryptography==45.0.5
 + curl-cffi==0.12.0
 + cyclopts==3.22.2
 + dnspython==2.7.0
 + docstring-parser==0.16
 + docutils==0.21.2
 + email-validator==2.2.0
 + exceptiongroup==1.3.0
 + fastapi==0.116.0
 + fastmcp==2.10.4
 + frozendict==2.4.6
 + multitasking==0.0.11
 + numpy==2.3.1
 + openapi-pydantic==0.5.1
 + pandas==2.3.1
 + peewee==3.18.2
 + platformdirs==4.3.8
 + protobuf==6.31.1
 + pycparser==2.22
 + pyperclip==1.9.0
 + python-dateutil==2.9.0.post0
 + pytz==2025.2
 + requests==2.32.4
 + rich-rst==1.3.1
 + six==1.17.0
 + soupsieve==2.7
 - starlette==0.47.1
 + starlette==0.46.2
 + tzdata==2025.2
 + urllib3==2.5.0
 + websockets==15.0.1
 + yfinance==0.2.65

(StockAnalysisServer) PS C:\WINDOWS\system32\StockAnalysisServer> uv --directory  C:\WINDOWS\system32\StockAnalysisServer run stock_mcp_server.py




********************************************************************************************
claude desktop-----> settings----> developer---> edit config--->claude_desktop_config.json

{
  "mcpServers": {
  
    "StockAnalysisServer": {
    
      "command": "uv",
      
      "args": [
      
        "--directory",
        
        "C:\\WINDOWS\\system32\\StockAnalysisServer",
        
        "run",
        
        "stock_mcp_server.py"
        
      ]
    }
  }
}

******************************************************************************************************
then see TOOLS
























































