import { confirmar } from './confirmacao.js'

document.querySelectorAll('form[data-confirmar]').forEach((form) => {
    form.addEventListener('submit', async (e) => {
        e.preventDefault()

        const confirmado = await confirmar({
            titulo: form.dataset.titulo,
            mensagem: form.dataset.mensagem,
            textoConfirmar: form.dataset.texto
        })

        if (confirmado) form.submit()
    })
})

