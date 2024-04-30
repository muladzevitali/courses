import { StyleSheet, View, Text, Pressable } from 'react-native'

const GoalItem = (props) => {
    return (

        <View style={styles.goalItem}>
            <Pressable
                android_ripple={{ color: "#dddddd" }}
                onPress={props.onDeleteItem.bind(this, props.goalItemData.id)}>
                <Text style={styles.goalText}>{props.goalItemData.text}</Text>
            </Pressable>
        </View >

    )
}



const styles = StyleSheet.create({
    goalItem: {
        margin: 8,
        borderRadius: 6,
        backgroundColor: "#5e0acc"
    },
    goalText: {
        color: "white",
        fontSize: 20,
        padding: 8,

    }
});

export default GoalItem