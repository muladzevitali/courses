import {useState} from 'react';

import Header from './components/Header.jsx';
import Shop from './components/Shop.jsx';
import {DUMMY_PRODUCTS} from './dummy-products.js';
import CartContextProvider from "./store/ShoppingCardContext.jsx";

function App() {
    const [shoppingCart, setShoppingCart] = useState({
        items: [],
    });


    return (
        <CartContextProvider>
            <Header
                cart={shoppingCart}
            />
            <Shop/>
        </CartContextProvider>
    );
}

export default App;
