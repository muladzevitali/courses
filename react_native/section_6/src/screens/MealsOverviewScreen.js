import { FlatList, StyleSheet, View } from "react-native"
import { useLayoutEffect } from 'react'
import { MEALS, CATEGORIES } from "../../data/dummy-data"
import MealItem from "../components/MealItem"

const MealsOverviewScreen = ({ route, navigation }) => {
    const categoryId = route.params.categoryId
    const displayedMeals = MEALS.filter(item => item.categoryIds.indexOf(categoryId) >= 0 ? true : false)

    useLayoutEffect(() => {
        const categoryTitle = CATEGORIES.find(item => item.id === categoryId).title

        navigation.setOptions({
            title: categoryTitle
        })
    }, [categoryId, navigation])


    const renderMealItem = (mealData) => {

        // const pressHandler = () => navigation.navigate('MealDetail', {mealId: mealData.item.id})
        const item = mealData.item
        const mealItemProps = {
            id: mealData.item.id,
            title: item.title,
            imageUrl: item.imageUrl,
            duration: item.duration,
            complexity: item.complexity,
            affordability: item.affordability
        }
        return <MealItem {...mealItemProps}/>
    }

    return <View style={styles.container}>
        <FlatList
            data={displayedMeals}
            keyExtractor={meal => meal.id}
            renderItem={renderMealItem}
        />
    </View>
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16
    }
})
export default MealsOverviewScreen