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
    axios.get('/api/product/colors/')
      .then(response => {
        this.colors = response.data
      })
  },

  getSize(color) {
    axios.get(`/api/product/${color}/sizes/`)
      .then(response => {
        this.sizes = response.data
        this.selectedColor = color
      })
  },

  getProductImage(size) {
    this.selectedSize = size.size
    axios.get(`/api/product/${this.selectedColor}/${this.selectedSize}/image/`)
      .then(response => {
        this.currentImage = response.data
          this.getSimilarProducts(this.selectedColor, this.selectedSize)
      })
  },

  getSimilarProducts(color, size){
    axios.get(`/api/products/${color}/${size}/`)
        .then(response => {
          this.similarProducts = response.data
            console.log(this.similarProducts)
        })
  },
})