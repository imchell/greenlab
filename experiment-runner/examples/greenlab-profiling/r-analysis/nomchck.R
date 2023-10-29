# Read the data from the CSV file
data <- read.csv("/Users/niczh/Courses/Y2P1 GreenLab/merged_result.csv")

# Split the data into two data frames based on the value of the GPT column
gpt_false_data <- data[data$GPT == "FALSE", ]
gpt_true_data <- data[data$GPT == "TRUE", ]

# Perform normality test on the "total_energy.J." column (control group)
shapiro_test_gpt_false <- shapiro.test(gpt_false_data$total_energy.J.)

# Perform normality test on the "total_energy.J." column (experimental group)
shapiro_test_gpt_true <- shapiro.test(gpt_true_data$total_energy.J.)

# Print the normality test results for the control group
print("Shapiro-Wilk Normality Test for GPT False Data:")
print("W =", shapiro_test_gpt_false$statistic)
print("p-value =", shapiro_test_gpt_false$p.value)

# Print the normality test results for the experimental group
print("Shapiro-Wilk Normality Test for GPT True Data:")
print(shapiro_test_gpt_true)

### Test for run time
# For hand-written code
shapiro_test_gpt_false <- shapiro.test(gpt_false_data$avg_disk_io)

# For GPT-generated code
shapiro_test_gpt_true <- shapiro.test(gpt_true_data$avg_disk_io)

# Set the layout for plots to 1 row and 2 columns
par(mfrow=c(1,2))

# Plot boxplot for energy consumption for GPT "TRUE" type
boxplot(total_energy.J. ~ Language, data = data[data$GPT == "TRUE",], 
        main = "True - Energy", xlab = "Language", ylab = "Energy")

# Plot boxplot for energy consumption for GPT "FALSE" type
boxplot(total_energy.J. ~ Language, data = data[data$GPT == "FALSE",], 
        main = "False - Energy", xlab = "Language", ylab = "Energy")

# Reset the default layout for plots
par(mfrow=c(1,1))

# Install the "gridExtra" package
install.packages("gridExtra")

# Load the required libraries
library(ggplot2)
library(gridExtra)

# Plot boxplot for GPT "TRUE" values
p1 <- ggplot(data[data$GPT == "TRUE",], aes(x=Language, y=total_energy.J., fill=Language)) +
  geom_boxplot() +
  labs(title="True - Energy", x="Language", y="Energy") +
  theme_minimal()

# Plot boxplot for GPT "FALSE" values
p2 <- ggplot(data[data$GPT == "FALSE",], aes(x=Language, y=total_energy.J., fill=Language)) +
  geom_boxplot() +
  labs(title="False - Energy", x="Language", y="Energy") +
  theme_minimal()

# Display the two plots side by side
grid.arrange(p1, p2, ncol=2)


library(gridExtra)

# Plot density graphs for various metric
p1 <- ggplot(data, aes(x=total_energy.J., fill=GPT)) + 
  geom_density(alpha=0.6, aes(color=GPT)) +
  labs(x="Energy Consumption (W)", y="Density") +
  scale_fill_manual(values=c("TRUE"="pink", "FALSE"="cyan")) +
  scale_color_manual(values=c("TRUE"="red", "FALSE"="blue")) +
  theme_minimal() +
  theme(legend.position=c(0.95, 0.95), legend.justification=c(1, 1))

p2 <- ggplot(data, aes(x=run_time, fill=GPT)) + 
  geom_density(alpha=0.6, aes(color=GPT)) +
  labs(x="Run Time (s)", y="Density") +
  scale_fill_manual(values=c("TRUE"="pink", "FALSE"="cyan")) +
  scale_color_manual(values=c("TRUE"="red", "FALSE"="blue")) +
  theme_minimal() +
  theme(legend.position=c(0.95, 0.95), legend.justification=c(1, 1))

p3 <- ggplot(data, aes(x=average_power.W., fill=GPT)) + 
  geom_density(alpha=0.6, aes(color=GPT)) +
  labs(x="Average Power(W)", y="Density") +
  scale_fill_manual(values=c("TRUE"="pink", "FALSE"="cyan")) +
  scale_color_manual(values=c("TRUE"="red", "FALSE"="blue")) +
  theme_minimal() +
  theme(legend.position=c(0.95, 0.95), legend.justification=c(1, 1))

p4 <- ggplot(data, aes(x=avg_cpu, fill=GPT)) + 
  geom_density(alpha=0.6, aes(color=GPT)) +
  labs(x="Mean CPU Load", y="Density") +
  scale_fill_manual(values=c("TRUE"="pink", "FALSE"="cyan")) +
  scale_color_manual(values=c("TRUE"="red", "FALSE"="blue")) +
  theme_minimal() +
  theme(legend.position=c(0.95, 0.95), legend.justification=c(1, 1))

p5 <- ggplot(data, aes(x=avg_mem, fill=GPT)) + 
  geom_density(alpha=0.6, aes(color=GPT)) +
  labs(x="Mean Memory Usage(Mb)", y="Density") +
  scale_fill_manual(values=c("TRUE"="pink", "FALSE"="cyan")) +
  scale_color_manual(values=c("TRUE"="red", "FALSE"="blue")) +
  theme_minimal() +
  theme(legend.position=c(0.95, 0.95), legend.justification=c(1, 1))

p6 <- ggplot(data, aes(x=avg_disk_io, fill=GPT)) + 
  geom_density(alpha=0.6, aes(color=GPT)) +
  labs(x="Mean Disk I/O (Byte/s)", y="Density") +
  scale_fill_manual(values=c("TRUE"="pink", "FALSE"="cyan")) +
  scale_color_manual(values=c("TRUE"="red", "FALSE"="blue")) +
  theme_minimal() +
  theme(legend.position=c(0.95, 0.95), legend.justification=c(1, 1))

# Combine the plots using grid.arrange
grid.arrange(p1, p2, p3, p4, p5, p6, ncol=3)
