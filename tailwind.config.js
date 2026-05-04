/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}", "./static/**/*.js"],
  theme: {
    extend: {
      colors: {
        cnec:{
          amarelo: {
            DEFAULT: '#ffd32b',
            escuro:'#d7b120',
          },
          azul: {
            DEFAULT: '#003C9D',
            claro: '#7c89c2',
            escuro: "#0e1133"
          },
          branco: '#F2F2F0'
        }
      },
      fontFamily: {
        poppins: ['Poppins', 'sans-serif']
      }
    },
  },
  plugins: [],
}

