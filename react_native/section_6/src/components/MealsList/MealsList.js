import { View, StyleSheet, FlatList } from "react-native"
import MealItem from "./MealItem"

const MealsList = ({ meals }) => {

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
        return <MealItem {...mealItemProps} />
    }

    return <View style={styles.container}>
        <FlatList
            data={meals}
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
export default MealsList