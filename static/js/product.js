const getItems = () => ({
    filteredItems: [],

    init() {
        this.getData()
    },

    getData() {
        axios.get('/api/product')
            .then(response => {
                console.log(response.data)
                this.filteredItems = response.data
            })
    }
})