<div align="center">
  <h1>Notion Kanban CLIpy</h1>
  <div align= "center">
    <h6>看板</h6>
  </div>
  <div align= "center">
    A CLI based script for a Kanban
  </div>
  <div align= "center">
    <a href="tox.ini"><img src="https://img.shields.io/pypi/pyversions/notion-client" alt="Supported Python Versions"></a>
  </div>
</div>
</br>

<div align= "center">
I've been using a Kanban on Notion ever since I needed to write down tasks for my every day life, but I couldn't stop thinking that sometimes I missed things just because I was too lazy to just open up notion, write down the thing I needed to do, and in case of doing it updating the Kanban accordingly, that's why I made this little silly CLI interface for my notion notes, feel free to try it your own    
</div>

<div align="center">
  <h3>Why using a CLI instead of the GUI?</h3>
    <p>To which I add... why not using both? that's what this CLI is pointing to you can still use the Kanban layout of this repository in Notion in fact that's something I promote but this aims to reduce the toiling of opening the browser on your own and doing manually </p>
</div align= "center">

<div align="center">
  <h3>So this is just like a TODO list but with no list?</h3>
    <img src="https://i.imgur.com/v1q728w.png">
    <p>yes</p>
</div align= "center">

## How to ⚙️ :
1. Duplicate the template from [here](https://boundless-heather-d8e.notion.site/63cd54d3b2254b02b9f258c52e38400a?v=8df3f9fdd3f446c8b2d89c794e29fd81) (right upper corner of the screen)
2. Create a notion integration, information [here](https://www.notion.so/my-integrations)
3. Once you copied the template you need to add the integration to the Kanban aka "Database" read [here](https://www.notion.so/my-integrations) specifically "step 2"
4. git clone `https://github.com/facundomartinezabeldano/Notion-CLI-Kanban`
5. `pip install -r requirements.txt`
6. The script will ask for your API key and database ID only the first time **MAKE SURE** to add those in src/userdata.json before running
7. run the script `python notionCLI.py`


TODO:
- [ ] Dockerize App

TODO (Code):
- [ ] Create the edit task function
- [ ] Testing maybe dunno
