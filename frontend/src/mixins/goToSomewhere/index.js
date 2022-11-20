export default {
    data() {
        return {}
    },
    created() {

    },
    methods: {
        goToRegister() {
            this.$router.push({name: 'Register'})
        },
        goToHistory() {
            this.$router.push({name: 'History'})
        },
        goToTransfer(id) {
            console.log(id)
            // перейти на страницу экспертов
            this.$router.push({name: 'Transfer', params: {id: id}})
        },
        goToProfile(id) {
            console.log(id)
            // перейти на страницу экспертов
            this.$router.push({name: 'ProfileView'})
        },
    }
}