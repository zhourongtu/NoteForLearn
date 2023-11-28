ALMRUN_CONFIG_PATH = ALMRUN_HOME .. "config\\"

--LUA���󲶻���
function error_hook(msg)
    message(msg:gsub("^(.+):(%d+):(.+)$","�ļ���%1\n������ [%2] �Ժ�����ݽ�������\n%3"),"Configure failed")
end

--ʹ��luajit��xpcall�����ÿ��Է���������������³������
function DoFile(file)
    xpcall(dofile,error_hook,file)
end

if FileExists('LuaEx/base.lua') then --������
    DoFile('LuaEx/base.lua')

    --��ȡ�û���չ��
    local Files = ListDir(ALMRUN_CONFIG_PATH,"*.lua",-1)
    if Files == nil then 
	return
    end
    for key,value in pairs(Files) do
	if value:find("[\\/]_",#ALMRUN_CONFIG_PATH) == nil then--������_��ͷ���ļ�/�ļ���
	    DoFile(value)
	end
    end
else
    MessageBox("LUA������LuaEx\\base.lua������,������LUA��չ����","LUA��չ")
end

if FileExists('LuaEx/update.lua') then
    DoFile('LuaEx/update.lua')
end