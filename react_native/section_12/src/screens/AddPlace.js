import PlaceForm from "../components/Places/PlaceForm"
import { insertPlace } from "../util/database"


const AddPlace = ({ navigation }) => {

    const createPlaceHandler = (place) => {
        insertPlace(place)
            .then(result => {
                console.log(result),
                    navigation.navigate('AllPlaces')
            })
            .catch(error => console.log(error))
    }

    return <PlaceForm onCreatePlace={createPlaceHandler} />
}

export default AddPlace