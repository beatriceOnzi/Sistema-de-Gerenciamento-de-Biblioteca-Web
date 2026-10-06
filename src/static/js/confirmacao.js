
export function confirmar({ titulo, mensagem, textoConfirmar } = {}) {
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