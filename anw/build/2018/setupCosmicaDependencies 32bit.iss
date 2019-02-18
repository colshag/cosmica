; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Cosmica Dependencies"
#define MyAppVersion "alpha"
#define MyAppPublisher "NeuroJump"
#define MyAppURL "www.playcosmica.com"
#define MyAppExeName "Cosmica Dependency Setup 32bit.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{962147EC-55DB-4A60-B0BF-6C079FE2B9A6}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
CreateAppDir=no
OutputDir=E:\development\COSMICA\anw\build\2018
OutputBaseFilename=Cosmica Dependency Setup
SetupIconFile=E:\development\COSMICA\anw\build\2018\app.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "E:\development\COSMICA\anw\build\2018\Panda3D-SDK-1.9.4.exe"; DestDir: "{win}"; Flags: ignoreversion
Source: "E:\development\COSMICA\anw\build\2018\Twisted-15.3.0.win32-py2.7.exe"; DestDir: "{win}"; Flags: ignoreversion
Source: "E:\development\COSMICA\anw\build\2018\zope.interface-4.1.3.win32-py2.7.exe"; DestDir: "{win}"; Flags: ignoreversion
Source: "E:\development\COSMICA\anw\build\2018\PyQt4-4.11.3-gpl-Py2.7-Qt4.8.6-x32.exe"; DestDir: "{win}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Run]
Filename: "{app}\Panda3D-SDK-1.9.4.exe"; StatusMsg: "Installing Panda 3D"; Flags: skipifsilent
Filename: "{app}\Twisted-15.3.0.win32-py2.7.exe"; StatusMsg: "Installing Twisted"; Flags: skipifsilent
Filename: "{app}\zope.interface-4.1.3.win32-py2.7.exe"; StatusMsg: "Installing Zope"; Flags: skipifsilent
Filename: "{app}\PyQt4-4.11.3-gpl-Py2.7-Qt4.8.6-x32.exe"; StatusMsg: "Installing Qt"; Flags: skipifsilent
