const getItems = () => ({
    filteredItems: [],
    sizes: ['P', 'M', 'G', 'GG'],
    currentImage: '',

    init() {
        this.getData()
    },

    getData() {
        axios.get('/api/v1/product')
            .then(response => {
                console.log(response.data[0].size)
                this.filteredItems = response.data
            })
    },

    getProduct(size, productId){
        //console.log(size);
        //console.log(productId);
        axios.get(`/api/v1/product/${productId}/image/${size.size}`)
        .then( response => {
            this.currentImage = response.data[0].image
            //console.log(this.currentImage)
            document.getElementById("imgChange").src = this.currentImage
        })
    }
})
