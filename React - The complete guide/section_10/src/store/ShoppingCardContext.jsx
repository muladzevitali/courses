import {createContext, useReducer, useState} from "react";
import {DUMMY_PRODUCTS} from "../dummy-products.js";

export const CartContext = createContext({
    items: [],
    addItem: () => {
    },
    updateItemQuantity: () => {
    }

})

const itemsReducer = (state, action) => {
    const updatedItems = [...state.items];

    switch (action.type) {
        case 'ADD_ITEM':
            const existingCartItemIndex = updatedItems.findIndex((cartItem) => cartItem.id === action.payload);
            const existingCartItem = updatedItems[existingCartItemIndex];

            if (existingCartItem) {
                updatedItems[existingCartItemIndex] = {
                    ...existingCartItem, quantity: existingCartItem.quantity + 1,
                };
            } else {
                const product = DUMMY_PRODUCTS.find((product) => product.id === action.payload);
                updatedItems.push({
                    id: action.payload, name: product.title, price: product.price, quantity: 1,
                });
            }

            return {items: updatedItems};
        case 'UPDATE_ITEM':
            const updatedItemIndex = updatedItems.findIndex((item) => item.id === action.payload.productId);

            const updatedItem = {
                ...updatedItems[updatedItemIndex],
            };

            updatedItem.quantity += action.payload.amount;

            if (updatedItem.quantity <= 0) {
                updatedItems.splice(updatedItemIndex, 1);
            } else {
                updatedItems[updatedItemIndex] = updatedItem;
            }

            return {items: updatedItems};
    }
    return state
}

const CartContextProvider = ({children}) => {
    const [itemsState, itemsDispatch] = useReducer(itemsReducer, {items: []})

    function handleAddItemToCart(id) {
        itemsDispatch({
            type: 'ADD_ITEM',
            payload: id

        })
    }

    function handleUpdateCartItemQuantity(productId, amount) {
        itemsDispatch({
            type: 'UPDATE_ITEM',
            payload: {
                productId,
                amount
            }
        })

    }

    const value = {
        items: itemsState.items, addItem: handleAddItemToCart, updateItemQuantity: handleUpdateCartItemQuantity

    }

    return <CartContext.Provider value={value}>
        {children}
    </CartContext.Provider>
}

export default CartContextProvider