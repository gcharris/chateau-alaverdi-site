import { useState } from 'react'
import './App.css'

function App() {
  const [email, setEmail] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    // Netlify will handle the form submission
    console.log('Form submitted with email:', email)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-cream via-white to-cream">
      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
        {/* Background Image */}
        <div className="absolute inset-0 z-0">
          <div className="w-full h-full bg-gradient-to-r from-bordeaux/20 to-gold/20"></div>
        </div>
        
        {/* Content */}
        <div className="relative z-10 max-w-6xl mx-auto px-6 text-center">
          <div className="mb-8">
            <h1 className="text-6xl md:text-8xl font-playfair font-bold text-bordeaux mb-4">
              Château Alaverdi
            </h1>
            <p className="text-2xl md:text-3xl font-playfair text-gold mb-2">1782</p>
            <p className="text-lg md:text-xl font-lato text-gray-700 max-w-2xl mx-auto">
              Nestled in the heart of Kakheti, Georgia, where tradition meets excellence in every bottle of Saperavi and Rkatsiteli
            </p>
          </div>

          {/* Wine Bottle Image */}
          <div className="mb-12">
            <div className="w-32 h-96 mx-auto bg-gradient-to-b from-bordeaux to-gold rounded-lg shadow-2xl flex items-center justify-center">
              <span className="text-white font-playfair text-sm rotate-90">Château Alaverdi</span>
            </div>
          </div>

          {/* CTA Section */}
          <div className="max-w-md mx-auto">
            <h2 className="text-2xl font-playfair text-bordeaux mb-6">
              Experience Georgian Wine Heritage
            </h2>
            
            {/* Netlify Form */}
            <form 
              name="contact" 
              method="POST" 
              data-netlify="true" 
              netlify-honeypot="bot-field"
              onSubmit={handleSubmit}
              className="flex flex-col gap-3 md:flex-row"
            >
              <input type="hidden" name="form-name" value="contact" />
              <div className="hidden">
                <label>Don't fill this out if you're human: <input name="bot-field" /></label>
              </div>
              
              <input 
                className="flex-1 h-11 border border-gray-300 px-3 rounded-md focus:outline-none focus:ring-2 focus:ring-bordeaux focus:border-transparent" 
                type="email" 
                name="email" 
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required 
                placeholder="you@company.com" 
              />
              <button 
                className="h-11 px-6 bg-bordeaux text-white rounded-md hover:bg-bordeaux/90 transition-colors font-lato font-medium" 
                type="submit"
              >
                Request Tasting
              </button>
            </form>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="py-20 bg-white">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <h2 className="text-4xl font-playfair text-bordeaux mb-8">
            A Legacy Since 1782
          </h2>
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <h3 className="text-2xl font-playfair text-gold mb-4">Our Heritage</h3>
              <p className="text-gray-700 font-lato leading-relaxed">
                For over two centuries, Château Alaverdi has been crafting exceptional wines in the Kakheti region of Georgia. 
                Our vineyards benefit from the unique terroir and traditional winemaking methods passed down through generations.
              </p>
            </div>
            <div>
              <h3 className="text-2xl font-playfair text-gold mb-4">Our Wines</h3>
              <p className="text-gray-700 font-lato leading-relaxed">
                We specialize in Georgia's signature varietals: the bold and complex Saperavi, and the elegant and aromatic Rkatsiteli. 
                Each bottle tells the story of our land and our commitment to excellence.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-bordeaux text-white py-12">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <h3 className="text-2xl font-playfair mb-4">Château Alaverdi</h3>
          <p className="font-lato text-cream mb-4">Kakheti, Georgia • Est. 1782</p>
          <p className="text-sm text-cream/80">
            Experience the taste of Georgian wine heritage
          </p>
        </div>
      </footer>
    </div>
  )
}

export default App