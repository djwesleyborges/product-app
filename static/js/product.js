const getItems = () => ({
  filteredItems: [],
  colors: [],
  sizes: [],
  currentImage: '',
  currentSize: '',

  init() {
    this.getData()
  },

  getData() {
    axios.get('/api/v1/product/colors/')
      .then(response => {
        this.colors = response.data
        console.log(this.colors)
        // const image = response.data[0].image[0].image
        // this.currentImage = `http://localhost:8000/${image}`
        // this.filteredItems = response.data
      })
  },

  getProductImage(size, productId) {
    axios.get(`/api/v1/product/${productId}/image/${size.size}`)
      .then(response => {
        this.currentImage = response.data[0].image
      })
  },

  // getImageColor(color, productId) {
  //   axios.get(`/api/v1/product/${productId}/color/${color.color}`)
  //     .then(response => {
  //       console.log(response)
  //       this.currentImage = response.data[0].image
  //     })
  // },

  getSize(color) {
    console.log(color)
    // Objetivo: retornar somente os tamanhos de cada cor.
    // axios.get(`/api/v1/product/${productId}/color/${color.color}`)
    //   .then(response => {
    //     console.log(response.data[0].size)
    //     this.currentSize = response.data[0].size
    //     console.log(`currentSize = ${this.currentSize}`)
    //   })
  },
})