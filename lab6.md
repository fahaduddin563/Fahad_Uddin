# Lab 6

## Task 1: Refactoring Questions

### Question 1

The refactoring method that should be used is **Extract Method**.  
The suspicious invoice behavior and the invoice printing behavior should be separated into smaller methods.

```java
public void printInvoiceDetails(Invoice invoice) {
    if (invoice.IsSuspicious) {
        handleSuspiciousInvoice(invoice);
        printInvoice(invoice);
    }
}

private void handleSuspiciousInvoice(Invoice invoice) {
    invoice.FlagCustomer = true;
    emailFinanceInvoice(invoice);
}

private void printInvoice(Invoice invoice) {
    System.out.println("Invoice ID: " + invoice.getId());
    System.out.println("Customer: " + invoice.getCustomerName());
    System.out.println("Amount: " + invoice.getAmount());
}
