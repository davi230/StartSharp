@echo off
title Instalar StartSharp na Inicialização

echo ===============================================
echo    Instalador Automatico StartSharp Inicializacao
echo ===============================================
echo.

echo Este script ira copiar o arquivo StartSharp.bat
echo para a pasta de Inicializacao do Windows do usuario atual.
echo Isso fará com que o StartSharp seja executado
echo automaticamente toda vez que o Windows iniciar.
echo.

rem Define o caminho completo do arquivo StartSharp.bat na pasta atual
rem %~dp0 expande para o caminho do diretorio onde este script (.bat) esta rodando
set "source_file=%~dp0StartSharp.bat"

rem Define o caminho da pasta de Inicializacao do Windows para o usuario atual
rem %APPDATA% e uma variavel de ambiente que aponta para AppData\Roaming
set "startup_folder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

echo Origem: %source_file%
echo Destino: %startup_folder%
echo.

rem Verifica se o arquivo StartSharp.bat existe na origem antes de tentar copiar
if not exist "%source_file%" (
    echo ERRO: O arquivo StartSharp.bat nao foi encontrado na pasta atual!
    echo Certifique-se de que este script (%~nx0) esta na mesma pasta que StartSharp.bat.
    goto end
)

rem Tenta criar o diretorio de destino caso nao exista (geralmente ja existe)
if not exist "%startup_folder%" mkdir "%startup_folder%"

rem Realiza a copia do arquivo
echo Copiando arquivo...
copy /y "%source_file%" "%startup_folder%"
echo.

rem Verifica se a copia foi bem sucedida
if exist "%startup_folder%\StartSharp.bat" (
    echo SUCESSO: StartSharp.bat foi copiado para a pasta de Inicializacao.
    echo Ele sera executado automaticamente na proxima vez que o Windows iniciar.
) else (
    echo ERRO: Nao foi possivel copiar o arquivo.
    echo Verifique as permissoes de escrita na pasta de destino:
    echo %startup_folder%
)

:end
echo.
echo Pressione qualquer tecla para fechar...
pause > nul