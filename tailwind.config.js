/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["src/templates/**/*.{html,js}", "./static/**/*.js"],
  theme: {
    extend: {
      colors: {
        cnec:{
          amarelo: {
            DEFAULT: '#f5c518',
            escuro:'#453501',
            shadow: "#c79d0e",
            claro: '#f5dd8e'
          },
          azul: {
            DEFAULT: '#003c9d',
            claro: {
              DEFAULT: '#6b7bb8',
              shadow: "#4F609C"
            },
            escuro: "#002054"
          },
          branco: '#f5f5f2'
        }
      },
      fontFamily: {
        poppins: ['Poppins', 'sans-serif']
      }
    },
  },
  plugins: [],
}