import { confirmar } from './confirmacao.js'

document.querySelectorAll('form[data-confirmar]').forEach((form) => {
    form.addEventListener('submit', async (e) => {
        e.preventDefault()

        const confirmado = await confirmar({
            titulo: 'Excluir cadastro?',
            mensagem: `Deseja realmente excluir "${form.dataset.nome}"? Todos os empréstimos realizados por esse aluno serão excluidos. Essa ação não pode ser desfeita.`,
            textoConfirmar: 'Sim, excluir'
        })

        if (confirmado) form.submit()
    })
})

