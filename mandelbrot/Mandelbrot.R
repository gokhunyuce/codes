# Mandelbrot Set Animation in R with Custom Output Folder
library(animation)
library(ggplot2)
library(reshape2)

# Timer start
t0 <- Sys.time()

# User input
cat("Enter parameters:\n")
x0 <- as.numeric(readline("x0: "))
x1 <- as.numeric(readline("x1: "))
y0 <- as.numeric(readline("y0: "))
y1 <- as.numeric(readline("y1: "))
n <- as.integer(readline("resolution: "))
max_iter <- as.integer(readline("maximum iteration: "))
output_folder <- readline("Output folder path (leave blank for current directory): ")

cat("Computing Mandelbrot frames...\n")

# Create grid
x <- seq(x0, x1, length.out = n)
y <- seq(y0, y1, length.out = n)
grid <- expand.grid(x = x, y = y)
C <- complex(real = grid$x, imaginary = grid$y)

# Initialize arrays
Z <- rep(0+0i, length(C))
K <- matrix(0, nrow = n, ncol = n)

# Precompute all frames
frames <- list()
for (i in 1:max_iter) {
  mask <- Mod(Z) <= 2
  Z[mask] <- Z[mask]^2 + C[mask]
  K[mask] <- i
  frames[[i]] <- matrix(K, nrow = n, ncol = n)
  cat(sprintf("\rComputed frame %d/%d", i, max_iter))
}

cat("\nSetting up animation...\n")

# Set output path
if (output_folder == "") {
  output_path <- "mandelbrot.gif"
} else {
  if (!dir.exists(output_folder)) {
    dir.create(output_folder, recursive = TRUE)
  }
  output_path <- file.path(output_folder, "mandelbrot.gif")
}

# Create animation
saveGIF({
  for (i in 1:max_iter) {
    df <- melt(frames[[i]])
    names(df) <- c("x", "y", "value")
    
    p <- ggplot(df, aes(x, y, fill = value)) +
      geom_raster(interpolate = TRUE) +
      scale_fill_gradientn(colors = heat.colors(256), limits = c(0, max_iter)) +
      coord_fixed() +
      ggtitle(sprintf("Mandelbrot Set (Iteration %d)", i)) +
      theme_minimal()
    
    print(p)
  }
}, movie.name = output_path, 
interval = 0.1, 
ani.width = 800, 
ani.height = 800)

cat("\nAnimation saved to:", normalizePath(output_path), "\n")

# Timer end
t1 <- Sys.time()
cat(sprintf("Total time: %.2f seconds\n", difftime(t1, t0, units = "secs")))