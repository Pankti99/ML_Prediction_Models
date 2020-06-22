This model returns which sales campaign will win. the Dataset used: sales-win-loss data available on IBM Watson.

The columns in our data set are strings, but the algorithms in scikit-learn understand only numeric data. So we require a method that converts this string data into numeric values.

The scikit-learn library provides us with many methods for converting string data into numerical data. One such method is the LabelEncoder() method. We have use this method to convert the categorical labels in our data set like ‘won’ and ‘loss’ into numerical labels.

First we imported the preprocessing module which provides the LabelEncoder() method. Then we created an object which represents the LabelEncoder() type. Next we used this object’s fit_transform() function to differentiate between different unique classes of the list  and First we imported the preprocessing module which provides the LabelEncoder() method. Then we created an object which represents the LabelEncoder() type. Next we used this object’s fit_transform() function to differentiate between different unique classes of the list ["won",  "loss"] then return a list with the respective encoded values, i.e. [1 0].


Now after we apply the modle , we got the results into numeric value. so we have to convert it back to categorial label. for that le.inverse_transform(pred[:20]) method is used.

