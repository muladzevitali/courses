import { View, Text, StyleSheet } from "react-native"

import { useContext } from "react"
import { FavouritesContext } from "../store/context/favourites-context"
import MealsList from "../components/MealsList/MealsList"
import { MEALS } from "../../data/dummy-data"
import { useSelector } from "react-redux"

const FavouritesScreen = () => {
    // const favouriteMealCtx = useContext(FavouritesContext)
    // const favouriteMealIds = favouriteMealCtx.ids

    const favouriteMealIds = useSelector(state => state.favouriteMeals.ids)
    const favouriteMeals = MEALS.filter(item => favouriteMealIds.includes(item.id))

    if (favouriteMeals.length === 0) {
        return <View style={styles.rootContainer}>
            <Text style={styles.text}>You have no favourite meals yet</Text>
        </View>
    }
    return <MealsList meals={favouriteMeals} />
}


const styles = StyleSheet.create({
    rootContainer: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center'
    },
    text: {
        fontSize: 18,
        fontWeight: 'bold',
        color: 'white'
    }
})
export default FavouritesScreen