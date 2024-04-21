package hse.course.android_lab2.adapter;

import android.annotation.SuppressLint;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

import hse.course.android_lab2.R;

public class ProductAdapter extends RecyclerView.Adapter<ProductAdapter.ProductViewHolder> {

    private final List<String> products;

    public static class ProductViewHolder extends RecyclerView.ViewHolder {

        private final TextView product;
        private final Button deleteButton;

        public ProductViewHolder(View view) {
            super(view);
            product = (TextView) view.findViewById(R.id.product);
            deleteButton = (Button) view.findViewById(R.id.deleteButton);
        }

        public TextView getProduct() {
            return product;
        }

        public Button getDeleteButton() {
            return deleteButton;
        }

    }

    public ProductAdapter(List<String> products) {
        this.products = products;
    }

    @NonNull
    @Override
    public ProductViewHolder onCreateViewHolder(ViewGroup viewGroup, int viewType) {
        View view = LayoutInflater.from(viewGroup.getContext()).inflate(R.layout.row_item, viewGroup, false);
        return new ProductViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ProductViewHolder holder, @SuppressLint("RecyclerView") int position) {
        holder.getProduct().setText(products.get(position));
        holder.getDeleteButton().setOnClickListener(v -> delete(position));
    }

    @Override
    public int getItemCount() {
        return products.size();
    }

    @SuppressLint("NotifyDataSetChanged")
    public void add(String productName) {
        if (productName == null || productName.isEmpty()) {
            return;
        }
        products.add(productName);
        notifyDataSetChanged();
    }

    @SuppressLint("NotifyDataSetChanged")
    public void delete(int position) {
        products.remove(position);
        notifyDataSetChanged();
    }

    @SuppressLint("NotifyDataSetChanged")
    public void remove() {
        products.clear();
        notifyDataSetChanged();
    }
}