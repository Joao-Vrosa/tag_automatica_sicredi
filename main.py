from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada
from time import sleep
from selenium.webdriver.common.keys import Keys
from pyautogui import press


def iniciar_driver():
    # Argumentos mais utilizados:
    """
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada) - Pode usar a máquina que nao quebrara a automação
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    """
    chrome_options = Options()
    argumentos = ['--lang=pt-BR', '--start-maximized', '--incognito']

    for argumento in argumentos:
        chrome_options.add_argument(argumento)

    # Uso de configurações experimentais:
    chrome_options.add_experimental_option('prefs', {
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir múltiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    # Inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    global wait  # Garantir que 'wait' seja acessível globalmente
    # Verificando se o elemento está visível, clicável ou se é existente - WAIT EXPLÍCITO
    wait = WebDriverWait(
        driver,
        10,  # Tempo de espera
        poll_frequency=1,  # Frequência de tentativas
        ignored_exceptions=[
            NoSuchElementException,  # Não encontrou o elemento
            ElementNotVisibleException,  # Elemento não está visível
            ElementNotSelectableException  # Elemento não está selecionável
        ]
    )

    return driver, wait


def login():
    try:
        # Botao entrar
        botao_entrar_login_inicial = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//button[@id="login-nexx-account"]')))
        botao_entrar_login_inicial.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    try:
        # Usuário
        user = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@id="username"]')))
        sleep(1)
        user.send_keys('USUARIO')
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    try:
        # Senha
        senha = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        sleep(1)
        senha.send_keys('SENHA')
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    sleep(1)

    try:
        # Botao segundario de entrar
        botao_entrar_login = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[@class="mdl-button__ripple-container"]')))
        botao_entrar_login.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    sleep(3)
    
    filtros()


def filtros():
    
    try:
        # Aba relacionamentos
        botao_relacionamento = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Relacionamento"]')))
        botao_relacionamento.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    sleep(2)

    ##################################### FILTRO - STATUS #####################################
    
    try:
        # Aba de filtros
        botao_filtros = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Código"]')))
        botao_filtros.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    sleep(1)

    try:
        # Mais filtros
        botao_mais_filtros = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Mais filtros"]')))
        botao_mais_filtros.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    sleep(2)

    try:
        # Inserindo filtros
        filtros_status = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Status"]')))
        filtros_status.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    sleep(1)

    try:
        # FILTRO - RECEBIDO
        status_recebido = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Recebido"]')))
        status_recebido.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    sleep(1)

    try:
        # FILTRO - EM ATENDIMENTO
        status_em_atendimento = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Em atendimento"]')))
        status_em_atendimento.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(1)

    try:
        # FILTRO - RELACIONAMENTO APROVADO
        status_relacionamento_aprovado = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Relacionamento aprovado"]')))
        status_relacionamento_aprovado.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(1)
    
    try:
        # FILTRO - PRONTO PARA IMPLANTAR
        status_pronto_para_implantar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Pronto para implantar"]')))
        status_pronto_para_implantar.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(1)
    
    try:
        # FILTRO - IMPLANTAÇÃO FINALIZADA
        status_implantacao_finalizada = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Implantação finalizada"]')))
        status_implantacao_finalizada.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    sleep(1)
    
    try:
        # FILTRO - FALHA NA IMPLANTAÇÃO
        status_falha_na_implantacao = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Falha na implantação"]')))
        status_falha_na_implantacao.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    sleep(1)

    # ESC para fechar o PopUp
    press('esc')
    press('esc')

    sleep(3)
    
    
    ##################################### FILTRO - SERVIÇOS #####################################
    try:
        servico = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Selecione"]')))
        servico.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')

    try:
        filtro_novo_relacionamento = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Novo relacionamento"]')))
        filtro_novo_relacionamento.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
    
    # ESC para fechar o PopUp
    press('esc')
    press('esc')
    
    sleep(3)
    
    
    ##################################### FILTRO - INSTITUIÇÃO #####################################
    try:
        instituicao = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Instituições"]')))
        instituicao.click()
        sleep(1)
        
        buscar_instituicao = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@placeholder="Buscar por Instituições"]')))
        buscar_instituicao.send_keys('Sicredi')
        sleep(1)
        
        selecionar_instituicao = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[contains(text(),"  Sicredi")] ')))
        selecionar_instituicao.click()
        sleep(1)
        
        press('esc')
        press('esc')
        
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(3)
    
    
    ##################################### FILTRO - RESPONSAVEL #####################################  
    try:
        responsavel = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Responsáveis"]')))
        responsavel.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    try:
        sem_atribuicao = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//mat-pseudo-checkbox[@class="mat-option-pseudo-checkbox mat-pseudo-checkbox ng-star-inserted"]')))
        sem_atribuicao.click()
        sleep(1)
        press('esc')
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(3)
    
    
    ##################################### APLICANDO FILTROS #####################################  
    try:
        aplicando_filtros = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//span[text()="Aplicar e salvar filtro"]')))
        aplicando_filtros.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(5)
    
    atribuir_responsavel()


def atribuir_responsavel():
    try:
        # Inserindo o maximo de itens por pagina
        itens_por_pagina = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-1"]/div/div[1]')))
        itens_por_pagina.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
        if True:
            driver.close()
    
    sleep(1)
    
    try:
        # Inserindo o maximo de itens por pagina
        itens_maximos = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="mat-option-34"]/span')))
        itens_maximos.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(5)
    
    try:
        # Selecionando todos os relacionamentos
        selecionar_todos = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="mat-checkbox-1"]/label')))
        selecionar_todos.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(1)
    
    try:
        # Clicando em AÇÕES
        acoes = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="add"]/span/span')))
        acoes.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(1)
        
    try:
        # Clicando em atribuir responsavel
        atribuir_responsavel_relacionamento = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Atribuir")]')))
        atribuir_responsavel_relacionamento.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(3)
    
    try:
        # Inserindo usuario responsavel
        inserir_usuario = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="mat-input-28"]')))
        # inserir_usuario.click()
        sleep(1)
        inserir_usuario.send_keys('USUARIO_RESPONSAVEL')
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM - {erro}')
        
    sleep(1)
    
    try:
        # Clicando no usuario inserido
        clicar_no_usuario = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//div[@class="truncate"]')))
        clicar_no_usuario.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM TESTE - {erro}')
        
    sleep(1)
    
    try:
        # Clicar em salvar
        clicar_em_salvar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="mat-dialog-1"]/pr-form-associate-user/form/mat-dialog-actions/button[2]/span/span')))
        clicar_em_salvar.click()
    except Exception as erro:
        print(f'[ERRO] Elemento não encontrado no DOM TESTE - {erro}')



if __name__ == "__main__":
    # Chamando a funcao para iniciar o driver
    driver, wait = iniciar_driver()

    # Navegar até um site
    driver.get('https://minhanexx.nexxera.io/welcome')
    
    login()


driver.close()
