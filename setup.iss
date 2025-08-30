; setup.iss
[Setup]
AppName=Radioactive Decay Simulator
AppVersion=1.0
AppPublisher=Gleb(glebario)
DefaultDirName={pf}\Radioactive Decay Simulator
DefaultGroupName=Radioactive Decay Simulator
OutputDir=output
OutputBaseFilename=Setup_Radioactive Decay Simulator
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\Radioactive Decay Simulator.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\Radioactive Decay Simulator"; Filename: "{app}\Radioactive Decay Simulator.exe"
