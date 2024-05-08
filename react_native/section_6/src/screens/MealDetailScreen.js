import { View, Text, Image, StyleSheet, ScrollView, Button } from "react-native"
import { MEALS } from "../../data/dummy-data"
import MealDetails from "../components/MealDetails"
import SubTitle from "../components/MealDetail/SubTitle"
import List from "../components/MealDetail/List"
import { useLayoutEffect } from "react"
import IconButton from "../components/IconButton"

const MealDetailScreen = ({ route, navigation }) => {
    const mealId = route.params.mealId
    const meal = MEALS.find(meal => meal.id === mealId)

    useLayoutEffect(() => {
        navigation.setOptions({
            headerRight: () => <IconButton icon='star' color='white' onPress={headerButtonPressHandler} />
        })
    }, [navigation, headerButtonPressHandler])

    const headerButtonPressHandler = () => {
        console.log('pressed')
    }
    return <ScrollView style={styles.rootContainer}>
        <Image source={{ uri: meal.imageUrl }} style={styles.image} />
        <Text style={styles.title}>{meal.title}</Text>
        <View>
            <MealDetails duration={meal.duration} complexity={meal.complexity} affordability={meal.affordability} />
        </View>
        <View style={styles.listOuterContainer}>
            <View style={styles.listContainer}>
                <SubTitle>Ingredients</SubTitle>
                <List data={meal.ingredients} />
                <SubTitle>Steps</SubTitle>
                <List data={meal.steps} />
            </View>
        </View>
    </ScrollView>
}

const styles = StyleSheet.create({
    rootContainer: {
        marginBottom: 32
    },
    image: {
        width: '100%',
        height: 350
    },
    title: {
        fontWeight: 'bold',
        fontSize: 24,
        margin: 8,
        textAlign: 'center',
    },
    detailText: {
        color: 'white'
    },
    listOuterContainer: {
        alignItems: 'center'
    },
    listContainer: {
        width: '80%'
    }
})

export default MealDetailScreen