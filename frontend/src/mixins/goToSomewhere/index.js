export default {
    data() {
        return {}
    },
    created() {

    },
    methods: {
        goToLogin() {
            this.$router.push({name: 'Login'})
        },
        goToRegister() {
            this.$router.push({name: 'Register'})
        },
        goToProfile(id) {
            console.log(id)
            // перейти на страницу экспертов
            this.$router.push({name: 'ProfileView'})
        },
        goToHistory() {
            this.$router.push({name: 'History'})
        },
        goToTransfer(id) {
            console.log(id)
            // перейти на страницу экспертов
            this.$router.push({name: 'Transfer', params: {id: id}})
        },
    }
}