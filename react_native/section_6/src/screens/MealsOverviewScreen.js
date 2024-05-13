import { FlatList, StyleSheet, View } from "react-native"
import { useLayoutEffect } from 'react'
import { MEALS, CATEGORIES } from "../../data/dummy-data"
import MealsList from "../components/MealsList/MealsList"

const MealsOverviewScreen = ({ route, navigation }) => {
    const categoryId = route.params.categoryId
    const displayedMeals = MEALS.filter(item => item.categoryIds.indexOf(categoryId) >= 0 ? true : false)

    useLayoutEffect(() => {
        const categoryTitle = CATEGORIES.find(item => item.id === categoryId).title

        navigation.setOptions({
            title: categoryTitle
        })
    }, [categoryId, navigation])


    return <MealsList meals={displayedMeals} />
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16
    }
})
export default MealsOverviewScreen