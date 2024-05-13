import { Text, View, Pressable, StyleSheet, Image, Platform } from "react-native";
import { useNavigation } from "@react-navigation/native";
import MealDetails from "../MealDetails";

const MealItem = ({ title, imageUrl, duration, complexity, affordability, id }) => {
    const navigation = useNavigation();
    const pressHandler = () => navigation.navigate('MealDetail', { mealId: id })

    return <View style={styles.mealItem}>
        <Pressable
            android_ripple={{ color: '#ccc' }}
            style={({ pressed }) => [
                pressed ? styles.buttonPressed : null
            ]}
            onPress={pressHandler}
        >
            <View style={styles.innerContainer}>
                <View>
                    <Image source={{ uri: imageUrl }} style={styles.image} />
                    <Text style={styles.title}>{title}</Text>
                </View>
                <MealDetails duration={duration} complexity={complexity} affordability={affordability}/>
            </View>
        </Pressable>
    </View>
}

const styles = StyleSheet.create({
    mealItem: {
        margin: 16,
        borderRadius: 8,
        backgroundColor: 'white',
        overflow: 'hidden',
        elevation: 4,
        overflow: Platform.OS === 'android' ? 'hidden' : 'visible'
    },
    innerContainer: {
        borderRadius: 8,
        overflow: 'hidden'
    },
    image: {
        widht: '100%',
        height: 200
    },
    title: {
        fontWeight: 'bold',
        textAlign: 'center',
        fontSize: 18,
        margin: 8
    },
    buttonPressed: {
        opacity: .5
    },
})

export default MealItem;