import { FlatList, StyleSheet, Text, View } from "react-native"
import PlaceItem from "./PlaceItem"
import { Colors } from "../../constants/colors"
import { useNavigation } from "@react-navigation/native"

const PlacesList = ({ places }) => {

    const navigation = useNavigation()

    if (!places || places.length === 0) {
        return <View style={styles.fallbackContainer}>
            <Text style={styles.fallbackText}>No places added yet</Text>
        </View>
    }

    const selectPlaceHandler = (placeId) => {
        navigation.navigate('PlaceDetails', { placeId: placeId })
    }

    return <FlatList
        style={styles.list}
        data={places}
        keyExtractor={item => item.id}
        renderItem={({ item }) => <PlaceItem place={item} onSelect={selectPlaceHandler} />}
    />
}

const styles = StyleSheet.create({
    list: {
        margin: 16
    },

    fallbackContainer: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center'
    },
    fallbackText: {
        fontSize: 16,
        color: Colors.primary200
    }
})

export default PlacesList