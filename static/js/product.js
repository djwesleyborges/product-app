const getItems = () => ({
    filteredItems: [],
    sizes: ['P', 'M', 'G', 'XG', 'GG'],

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