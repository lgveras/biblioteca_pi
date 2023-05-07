// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    css: [
        'vuetify/lib/styles/main.sass',
        '@mdi/font/css/materialdesignicons.min.css',
    ],
    build: {
        transpile: ['vuetify'],
    },
    modules: [
        '@nuxtjs/google-fonts',        
    ],
    googleFonts: {
        families: {
            Montserrat: true,
        },
        subsets: ['latin'],
        display: 'swap',
        prefetch: false,
        preconnect: false,
        preload: false,
        download: true,    
    }
})
