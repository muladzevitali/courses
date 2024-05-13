import { createContext, useState } from "react";

export const FavouritesContext = createContext({
    ids: [],
    addFavourite: (id) => { },
    removeFavourite: (id) => { }
})

const FavouritesContextProvider = ({ children }) => {
    const [favouriteMealIds, setFavouriteMealIds] = useState([])

    function addFavourite(id) {
        setFavouriteMealIds((prevIds) => [...prevIds, id])
    }

    function removeFavourite(id) {
        setFavouriteMealIds((prevIds) => prevIds.filter((mealId) => mealId !== id))
    }
    const value = {
        ids: favouriteMealIds,
        addFavourite: addFavourite,
        removeFavourite: removeFavourite
    }

    return <FavouritesContext.Provider
        value={value}
    >
        {children}
    </FavouritesContext.Provider>
}

export default FavouritesContextProvider;