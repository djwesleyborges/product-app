const getItems = () => ({
    colors: [],
    sizes: [],
    currentImage: {},
    selectedColor: null,
    selectedSize: null,
    similarProducts: [],

    init() {
        this.getData()
    },

    getData() {
        axios.get('/api/v1/product/colors/')
            .then(response => {
                this.colors = response.data
            })
    },

    getSize(color) {
        axios.get(`/api/v1/product/${color}/sizes/`)
            .then(response => {
                this.sizes = response.data
                this.selectedColor = color
            })
    },

    getProductImage(size) {
        this.selectedSize = size.size
        axios.get(`/api/v1/product/${this.selectedColor}/${this.selectedSize}/image/`)
            .then(response => {
                this.currentImage = response.data
                this.getSimilarProducts(this.selectedColor, this.selectedSize)
            })
    },

    getSimilarProducts(color, size) {
        axios.get(`/api/v1/products/${color}/${size}/`)
            .then(response => {
                this.similarProducts = response.data
                console.log(this.similarProducts)
            })
    },
})

const appProdutc = () => ({

    products: [],
    listProducts: [],

    init() {
        this.getProduct()
    },

    getProduct() {
        axios.get(`/api/v1/product`)
            .then(response => {
                this.products = response.data
            })
    },

    addRow() {
        this.listProducts.push({
            'product': '',
            'quantity': null,
            'price': null
        })
    },

    getPrice(product, index) {
        const item = this.products.find((item) => {
            return item.id = product
        })
        if (item) this.listProducts[index].price = item.price
    },
})