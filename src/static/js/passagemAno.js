const avancarAno_btn = document.getElementById('avancarAno')

avancarAno_btn.addEventListener('click', avancarAno)

async function avancarAno() {
    if (avancarAno_btn.dataset.processando === 'true') return

    const confirmado = await confirmar({
        titulo: 'Avançar as Turmas?',
        mensagem: 'Essa ação passará todos os alunos para a turma seguinte. Deseja continuar?',
        textoConfirmar: 'Sim, avançar'
    })

    if (!confirmado) return

    definirCarregando(true)

    try {
        const response = await fetch('./avancarAno')
        const data = await response.json()

        if (response.ok) {
            mostrarRetorno(data, 'sucesso')
        } else {
            mostrarRetorno(data, 'erro')
        }
    } catch (err) {
        mostrarRetorno('Erro de conexão.', 'erro')
    } finally {
        definirCarregando(false)
    }
}


function definirCarregando(estaCarregando) {
    avancarAno_btn.dataset.processando = estaCarregando ? 'true' : 'false'
    avancarAno_btn.classList.toggle('opacity-50', estaCarregando)
    avancarAno_btn.classList.toggle('pointer-events-none', estaCarregando)
}

function confirmar({ titulo, mensagem, textoConfirmar } = {}) {
    return new Promise((resolve) => {
        const overlay = document.getElementById('confirmacao')
        const box = document.getElementById('box')
        const confirmar_btn = document.getElementById('confirmar_btn')
        const cancelar_btn = document.getElementById('cancelar_btn')

        document.getElementById('titulo').textContent = titulo
        document.getElementById('mensagem').textContent = mensagem
        confirmar_btn.textContent = textoConfirmar
        confirmar_btn.disabled = false

        abrirConfirmacao(overlay, box)

        function onConfirmar() {
            confirmar_btn.disabled = true
            fechar(true)
        }

        function onCancelar() {
            fechar(false)
        }

        function fechar(resultado) {
            fecharConfirmacao(overlay, box)
            confirmar_btn.removeEventListener('click', onConfirmar)
            cancelar_btn.removeEventListener('click', onCancelar)
            resolve(resultado)
        }

        confirmar_btn.addEventListener('click', onConfirmar)
        cancelar_btn.addEventListener('click', onCancelar)
    })
}

function abrirConfirmacao(overlay, box) {
    overlay.classList.remove('opacity-0', 'pointer-events-none')
    requestAnimationFrame(() => {
        overlay.classList.add('opacity-100')
        box.classList.remove('scale-95')
        box.classList.add('scale-100')
    })
}

function fecharConfirmacao(overlay, box) {
    overlay.classList.remove('opacity-100')
    box.classList.remove('scale-100')
    box.classList.add('scale-95')
    setTimeout(() => overlay.classList.add('opacity-0', 'pointer-events-none'), 200)
}

function mostrarRetorno(mensagem, tipo) {
    const retorno = document.getElementById('retorno')

    retorno.textContent = mensagem
    retorno.classList.remove('bg-green-600', 'bg-red-600')
    retorno.classList.add(tipo === 'erro' ? 'bg-red-600' : 'bg-green-600')

    retorno.classList.remove('opacity-0', '-translate-y-5', 'pointer-events-none')
    retorno.classList.add('opacity-100', 'translate-y-0')

    setTimeout(() => {
        retorno.classList.remove('opacity-100', 'translate-y-0')
        retorno.classList.add('opacity-0', '-translate-y-5', 'pointer-events-none')
    }, 3000)
}