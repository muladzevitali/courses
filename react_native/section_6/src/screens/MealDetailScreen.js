import { View, Text, Image, StyleSheet, ScrollView, Button } from "react-native"
import { MEALS } from "../../data/dummy-data"
import MealDetails from "../components/MealDetails"
import SubTitle from "../components/MealDetail/SubTitle"
import List from "../components/MealDetail/List"
import { useContext, useLayoutEffect } from "react"
import IconButton from "../components/IconButton"
import { FavouritesContext } from "../store/context/favourites-context"
import { useDispatch, useSelector } from "react-redux"
import { addFavourite, remo, removeFavourite } from "../store/redux/favourites"

const MealDetailScreen = ({ route, navigation }) => {
    const mealId = route.params.mealId
    const meal = MEALS.find(meal => meal.id === mealId)

    // const favouriteMealCtx = useContext(FavouritesContext)

    const favouriteMealIds = useSelector((state) => state.favouriteMeals.ids)
    const dispatch = useDispatch()

    // const mealIsFavourite = favouriteMealCtx.ids.includes(mealId)
    const mealIsFavourite = favouriteMealIds.includes(mealId)

    useLayoutEffect(() => {
        navigation.setOptions({
            headerRight: () => <IconButton
                icon={mealIsFavourite ? 'star' : 'star-outline'}
                color='white'
                onPress={changeFavouriteStatusHandler}
            />
        })
    }, [navigation, mealIsFavourite, changeFavouriteStatusHandler])

    const changeFavouriteStatusHandler = () => {
        if (mealIsFavourite) {
            // favouriteMealCtx.removeFavourite(mealId)
            dispatch(removeFavourite({id: mealId}))
        } else {
            // favouriteMealCtx.addFavourite(mealId)
            dispatch(addFavourite({id: mealId}))
        }
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