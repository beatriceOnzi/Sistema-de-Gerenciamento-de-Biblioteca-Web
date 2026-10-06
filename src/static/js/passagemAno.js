import { confirmar } from './confirmacao.js'

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